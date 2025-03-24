"""
Rainfall and World classes to fetch and analyze rainfall data.

To be reorganized/refactored as part of the larger code as we merge things together.

By Irem Altan.
"""
import requests, os, pathlib, shutil
import zipfile, gzip
from statistics import mean

import cv2
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

import geopandas as gpd
from shapely.geometry import Point

def movmean(nums, window=5):
    """Function that calculates the moving mean of a list of numbers."""
    # implement a simple moving mean
    assert (window > 0)
    assert (isinstance(window, int))

    # check if nums is a list of numbers
    if np.isscalar(nums):
        raise TypeError("ERROR: you must provide a list or array of numbers for calculating moving mean.")

    # determine radius
    if window % 2 != 0:
        left_r = window // 2
        right_r = window // 2
    else:
        # matlab style
        left_r = window // 2
        right_r = window // 2 - 1

    averaged = []
    for i in range(len(nums)):
        start = max(i - left_r, 0)
        end = min(i + right_r, len(nums))

        averaged.append(mean(nums[start:end + 1]))

    return averaged

class Rainfall:
    """
    The Rainfall class has functions to fetch CRU gridded data and analyze per month.
    """
    def __init__(self, stem='https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.08/cruts.2406270035.v4.08/pre/cru_ts4.08.'):
        self.stem = stem
        self.start_year = None
        self.end_year = None
        self.data = None

    def fetch_data_years(self, start_year, end_year, extract_to='data', delete_file=False):
        """
        Fetch data given a start_year and end_year. Note that files for an arbitrary range
        does not exist. Typically, files exist in 10-year ranges: e.g. 1901-1910.        
        """
        url = f"{self.stem}{start_year}.{end_year}.pre.dat.gz"

        # TODO: use pathlib to do this cleanly?
        if extract_to.endswith('/'):
            extract_to = extract_to[:-1]

        # create extraction folder if it does not exist
        if not os.path.isdir(extract_to):
            os.mkdir(extract_to)

        # check the suffix
        suffix = pathlib.Path(url).suffix

        # get the file name without suffix
        filename = pathlib.Path(url).stem

        # fetch and unzip, if necessary
        try:
            response = requests.get(url)
            response.raise_for_status()

            with open(f"{extract_to}/{filename}{suffix}", 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            if suffix == '.gz':
                with gzip.open(f"{extract_to}/{filename}{suffix}", 'rb') as f_in:
                    with open(f"{extract_to}/{filename}", 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                os.remove(f"{extract_to}/{filename}{suffix}")
            
            self.data = np.loadtxt(f"{extract_to}/{filename}")
            self.start_year = start_year
            self.end_year = end_year

            # clean up, if requested
            if delete_file:
                os.remove(f"{extract_to}/{filename}")
                # remove the folder if empty
                if len(os.listdir(extract_to)) == 0:
                    os.rmdir(extract_to)

        # print out error if we encounter one
        except requests.exceptions.RequestException as e:
            print("Error downloading file: {e}")
        return

    def get_month(self, month: int, year: int):
        """
        Get the numpy array containing rainfall totals in each grid point,
        given a month and a year.
        """
        if year > self.end_year or year < self.start_year:
            raise ValueError(f"The year queried ({year}) isn't in the range of data ({self.start_year},{self.end_year}).")
        
        if month > 12 or month <= 0:
            raise ValueError(f'{month} is not a valid month. Please enter 1-12.')
        
        # get the shape of the output array
        m, n = self.data.shape
        sy = n
        sx = m // ((self.end_year - self.start_year + 1)*12)

        # calculate the index for slicing the whole data
        idx = (year - self.start_year)*12 + (month - 1)

        return self.data[idx*sx:(idx+1)*sx,:]

    def plot_month(self, month: int, year: int):
        """
        Given a month and a year, return ax object that plots totals as a heatmap.
        """
        data = self.get_month(month, year)

        rotated = cv2.rotate(data.T, cv2.ROTATE_90_COUNTERCLOCKWISE)
        fig, ax = plt.subplots(figsize=(12,6))
        ax.imshow(rotated)
        ax.set(xticks=np.arange(0, 720, 40),
               xticklabels=np.arange(-180, 180, 20))
        ax.set(yticks=np.arange(0, 360, 20),
               yticklabels=np.arange(90, -90, -10))

        ax.set_xlabel('Lattitude')
        ax.set_ylabel('Longitude')
        ax.axhline(180, color='red', linestyle='dashed')
        ax.axvline(360, color='red', linestyle='dashed')
        ax.set_title(f'Rainfall {month}-{year}')
        return ax
    
    def get_country_total_at_time(self, month: int, year: int, iso_code:str, world) -> float:
        """
        Given a month and a year, and the iso_code of a country, return the total
        rainfall in that country.
        """
        data = self.get_month(month, year)
        idx = world.get_grid_points_of_country(iso_code)
        return np.sum(data[idx])
    
    def get_country_total(self, month_range, year_range, iso_code, world):
        t = []
        dates = []
        totals = []
        ct = 0
        for year in range(year_range[0], year_range[1]+1):
            if year == year_range[0]:
                m_s = month_range[0]
            else:
                m_s = 1
            if year == year_range[1]:
                m_e = month_range[1]
            else:
                m_e = 12
            for month in range(m_s, m_e + 1):
                total = self.get_country_total_at_time(month, year, iso_code, world)
                totals.append(total)
                t.append(ct)
                dates.append(f'{month}-{year}')
                ct += 1

        return t, dates, totals
    
    def get_country_winter_mean(self, year_range, iso_code, world):
        years = []
        new_t = []
        winter_means = []
        for i, yr in enumerate(range(year_range[0], year_range[1])):
            t, dates, totals = self.get_country_total((1,12),(yr, yr+1), iso_code, world)
            new_t.append(i)
            years.append(f'{yr}-{yr+1}')
            winter_means.append(np.mean(totals[10:11+4]))
            
            # TODO: move to tests
            assert dates[10] == f'11-{yr}'
            assert dates[15] == f'4-{yr+1}'

        return new_t, years, winter_means


class World:
    """
    Class to allow for quick country lookup given a coordinate.
    """
    def __init__(self, shape_file):
        self.world = gpd.read_file(shape_file)

        self.idx_to_iso = {}
        self.iso_to_idx = {}
        self.world_array = None
        self.sindex = None

        self.create_sindex()

    def create_sindex(self):
        """Utilize R-trees for quick lookup."""
        self.sindex = self.world.sindex

    def get_country_from_shp(self, lon: float, lat: float):
        """
        Get the country object corresponding to lon & lat, utilizing the shape file.
        """
        point = Point(lon, lat)
        
        possible_matches = list(self.sindex.intersection(point.bounds))

        for idx in possible_matches:
            country = self.world.iloc[idx]
            if country['geometry'].contains(point):
                return country

        return None

    def create_lookup(self, grid_spacing=0.5):
        """
        Create an (n by m) array and two dictionaries for a quick lookup.
        
        grid_spacing is in degrees. The default value creates a grid that is the same
        size as the CRU data.
        """
        nlat = int(180 / 0.5)
        nlon = int(360 / 0.5)

        self.world_array = np.zeros((nlat, nlon))

        country_idx = 0
        for i, lat in enumerate(np.arange(-90, 90, grid_spacing)):
            for j, lon in enumerate(np.arange(-180, 180, grid_spacing)):
                country = self.get_country_from_shp(lon, lat)
                if country is None:
                    self.world_array[i,j] = -1
                else:
                    iso = country['SOV_A3']
                    if iso in self.iso_to_idx:
                        idx = self.iso_to_idx[iso]
                        self.world_array[i,j] = idx
                    else:
                        idx = country_idx
                        self.iso_to_idx[iso] = idx
                        self.idx_to_iso[idx] = iso
                        self.world_array[i,j] = idx
                        country_idx += 1
        return

    def get_country_by_index(self, i: int, j: int) -> str:
        """
        Get the ISO code of the country given a point on the grid.
        """
        if self.world_array is None:
            raise ValueError('Please run create_lookup() first')

        idx = self.world_array[i,j]
        return self.idx_to_iso[idx]

    def get_grid_points_of_country(self, iso_code: str):
        """
        Get indices all grid points that correspond to a specific country.
        """
        if self.world_array is None:
            raise ValueError('Please run create_lookup() first')

        idx = self.iso_to_idx[iso_code]
        return np.where(self.world_array == idx)
    
def diff(arr, lag=0):
    """
    For calculating Delta R_{i,t}. Here, if lag is nonzero, we consider
    Delta R_{i,t-lag}.
    """
    if lag >= len(arr)-1:
        raise ValueError(f'Lag:{lag} and length of array:{len(arr)}.')

    arr = np.array(arr)
    arr_t = arr[1:]
    arr_t_1 = arr[:-1]

    res = (arr_t - arr_t_1)/(arr_t_1)
    if lag == 0:
        return res
    return res[:-lag]
    
class CsvFetcher:
    def __init__(self, url):
        self.url = url
        
    def fetch(self, file_name='temp.csv', extract_to='data', delete_file=True):
        """
        TODO: refactor (because it rewrites a lot of the functionality of the Rainfall
        fetcher).
        """
        if extract_to.endswith('/'):
            extract_to = extract_to[:-1]

        if not os.path.isdir(extract_to):
            os.mkdir(extract_to)

        # TODO: more detailed error handling (e.g. check url first)
        try:
            response = requests.get(self.url)
            response.raise_for_status()

            with open(f"{extract_to}/{file_name}", 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            data_frame = pd.read_csv(f"{extract_to}/{file_name}")

            if delete_file:
                os.remove(f"{extract_to}/{file_name}")
                if len(os.listdir(extract_to)) == 0:
                    os.rmdir(extract_to)
            return data_frame
        except requests.exceptions.RequestException as e:
            print("Error downloading file: {e}")
            raise e
        