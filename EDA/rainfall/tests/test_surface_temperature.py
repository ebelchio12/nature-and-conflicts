import sys

import tempfile

sys.path.insert(0, '.')
sys.path.insert(1, '..')

from grid_data import SurfaceTemperature

class TestSurfaceTemperature:
    def test_init(self):
        surf_temp = SurfaceTemperature()

    def test_fetch(self):
        surf_temp = SurfaceTemperature()

        with tempfile.TemporaryDirectory() as tmpdirname:
            surf_temp.fetch_data_years(1901, 1910, extract_to=tmpdirname)

        assert surf_temp.start_year == 1901
        assert surf_temp.end_year == 1910

    def test_get_month(self):
        surf_temp = SurfaceTemperature()

        with tempfile.TemporaryDirectory() as tmpdirname:
            surf_temp.fetch_data_years(1901, 1910, extract_to=tmpdirname)

        res = surf_temp.get_month(5, 1902)
        assert res.shape[0] == 360
        assert res.shape[1] == 720