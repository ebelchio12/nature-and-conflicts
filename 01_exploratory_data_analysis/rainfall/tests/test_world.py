import sys
import numpy as np

import tempfile

sys.path.insert(0, '.')
sys.path.insert(1, '..')

from world import World

class TestWorld:
    def test_init(self):
        world = World('aux_files/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')

    def test_get_country_from_shp(self):
        world = World('aux_files/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
        res = world.get_country_from_shp(85.137566, 25.594095)
        assert res['SOV_A3'] == 'IND'
        
        res = world.get_country_from_shp(90,-90)
        assert res is None

    def test_create_lookup(self):
        world = World('aux_files/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
        world.create_lookup()

    def test_get_grid_points_of_country(self):
        world = World('aux_files/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
        world.create_lookup()

        res = world.get_grid_points_of_country('IND')

        chosen = world.world_array[res]
        idx = world.iso_to_idx['IND']

        assert np.all(chosen==idx)
