import requests, os, pathlib, shutil
import zipfile, gzip

import cv2
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

from world import World

class GridData:
    """
    Parent GridData class to fetch and analyze CRU data.
    """
    def __init__(self, stem):
        self.stem = stem
        self.start_year = None
        self.end_year = None
        self.data = None

    def fetch_data_years(self, start_year, end_year, data_type, extract_to='data', delete_file=False):
        """
        Fetch data given a start_year and end_year. Note that files for an arbitrary range
        does not exist. Typically, files exist in 10-year ranges: e.g. 1901-1910.        
        """
        url = f"{self.stem}{start_year}.{end_year}.{data_type}.dat.gz"

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
        Get the numpy array containing data in each grid point,
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
    
    def prep_to_plot(self, month: int, year: int):
        """
        Given a month and a year, return transformed data ready to plot.
        """
        data = self.get_month(month, year)

        rotated = cv2.rotate(data.T, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return rotated
    
    def get_country_avg_at_time(self, month: int, year: int, iso_code: str, world) -> float:
        """
        Given a month and a year, and the iso_code of a country, return the average of grid points
        in that country.
        """
        data = self.get_month(month, year)
        idx = world.get_grid_points_of_country(iso_code)
        vals = data[idx]
        idx2 = np.where(vals != -999)
        return np.mean(vals[idx2])
    
    def get_country_avg(self, month_range, year_range, iso_code, world):
        t = []
        dates = []
        averages = []
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
                avg = self.get_country_avg_at_time(month, year, iso_code, world)
                averages.append(avg)
                t.append(ct)
                dates.append(f'{month}-{year}')
                ct += 1

        return t, dates, averages
    
    def get_country_annual_avg(self, year_range, iso_code, world):
        t = []
        years = []
        averages = []
        ct = 0

        for year in range(year_range[0], year_range[1] + 1):
            annual = []
            for month in range(1, 13):
                avg = self.get_country_avg_at_time(month, year, iso_code, world)
                annual.append(avg)
            averages.append(np.mean(annual))
            t.append(ct)
            ct += 1
            years.append(year)

        return t, years, averages
    

class Rainfall(GridData):
    """
    Rainfall class that inherits from GridData.
    """
    def __init__(self, stem='https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.08/cruts.2406270035.v4.08/pre/cru_ts4.08.'):
        super().__init__(stem)

    def fetch_data_years(self, start_year, end_year, data_type='pre', extract_to='data', delete_file=False):
        super().fetch_data_years(start_year, end_year, data_type, extract_to, delete_file)
    
    def plot_month(self, month: int, year: int):
        """
        Plot heatmap of rainfall totals in a month.
        """
        data = self.prep_to_plot(month, year)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.imshow(data)
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
    
    def get_country_winter_mean(self, year_range, iso_code, world):
        """
        TODO!!!: add a check for southern hemisphere.
        """
        years = []
        new_t = []
        winter_means = []
        for i, yr in enumerate(range(year_range[0], year_range[1])):
            t, dates, avgs = self.get_country_avg((1,12), (yr, yr+1), iso_code, world)
            new_t.append(i)
            years.append(f'{yr}-{yr+1}')
            winter_means.append(np.mean(avgs[10:11+4]))

            # TODO: move to tests
            assert dates[10] == f'11-{yr}'
            assert dates[15] == f'4-{yr+1}'

        return new_t, years, winter_means
    
class SurfaceTemperature(GridData):
    """
    Surface temperature class that inherits from GridData.
    """
    def __init__(self, stem='https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.08/cruts.2406270035.v4.08/tmp/cru_ts4.08.'):
        super().__init__(stem)

    def fetch_data_years(self, start_year, end_year, data_type='tmp', extract_to='data', delete_file=False):
        super().fetch_data_years(start_year, end_year, data_type, extract_to, delete_file)

    def plot_month(self, month: int, year: int):
        """
        Plot heatmap of surface temperature averages in the given month.
        """
        data = self.prep_to_plot(month, year)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.imshow(data)
        ax.set(xticks=np.arange(0, 720, 40),
               xticklabels=np.arange(-180, 180, 20))
        ax.set(yticks=np.arange(0, 360, 20),
               yticklabels=np.arange(90, -90, -10))

        ax.set_xlabel('Lattitude')
        ax.set_ylabel('Longitude')
        ax.axhline(180, color='red', linestyle='dashed')
        ax.axvline(360, color='red', linestyle='dashed')
        ax.set_title(f'Surface Temperature {month}-{year}')
        return ax