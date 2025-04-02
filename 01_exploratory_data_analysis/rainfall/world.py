import geopandas as gpd
from shapely.geometry import Point

import numpy as np

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