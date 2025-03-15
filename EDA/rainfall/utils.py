import requests, os, pathlib, shutil
import zipfile, gzip

import numpy as np
import pandas as pd

import geopandas as gpd
from shapely.geometry import Point

class Rainfall:
    def __init__(self, stem='https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.08/cruts.2406270035.v4.08/pre/cru_ts4.08.'):
        self.stem = stem
        self.start_year = None
        self.end_year = None
        self.data = None

    def fetch_data_years(self, start_year, end_year, extract_to='data', delete_file=False):
        url = f"{self.stem}{start_year}.{end_year}.pre.dat.gz"

        if extract_to.endswith('/'):
            extract_to = extract_to[:-1]

        if not os.path.isdir(extract_to):
            os.mkdir(extract_to)

        # check the suffix
        suffix = pathlib.Path(url).suffix

        filename = pathlib.Path(url).stem

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
            if delete_file:
                os.remove(f"{extract_to}/{filename}")

        except requests.exceptions.RequestException as e:
            print("Error downloading file: {e}")
        return

    def get_month(self, month: int, year: int):
        if year > self.end_year or year < self.start_year:
            raise ValueError(f"The year queried ({year}) isn't in the range of data ({self.start_year},{self.end_year}).")

        month = month % 12

        m, n = self.data.shape
        sy = n
        sx = m // ((self.end_year - self.start_year + 1)*12)

        idx = (year - self.start_year)*12 + month

        return self.data[idx*sx:(idx+1)*sx,:]

class World:
    def __init__(self, shape_file):
        self.world = gpd.read_file(shape_file)
        self.idx_to_iso = {}
        self.iso_to_idx = {}
        self.world_array = None
        self.sindex = None

        self.create_sindex()

    def create_sindex(self):
        self.sindex = self.world.sindex

    def get_country_from_shp(self, lon: float, lat: float):
        point = Point(lon, lat)
        
        possible_matches = list(self.sindex.intersection(point.bounds))

        for idx in possible_matches:
            country = self.world.iloc[idx]
            if country['geometry'].contains(point):
                return country

        return None

    def create_lookup(self, grid_spacing=0.5):
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
        if self.world_array is None:
            raise ValueError('Please run create_lookup() first')

        idx = self.world_array[i,j]
        return self.idx_to_iso[idx]

    def get_grid_points_of_country(self, iso_code: str):
        if self.world_array is None:
            raise ValueError('Please run create_lookup() first')

        idx = self.iso_to_idx[iso_code]
        return np.where(self.world_array == idx)


