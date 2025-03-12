import sys

import tempfile

sys.path.insert(0, '.')
sys.path.insert(1, '..')

from utils import Rainfall

class TestRainfall:
    def test_init(self):
        rainfall = Rainfall()

    def test_fetch(self):
        rainfall = Rainfall()
        
        with tempfile.TemporaryDirectory() as tmpdirname:
            rainfall.fetch_data_years(1901, 1910, extract_to=tmpdirname)

        assert rainfall.start_year == 1901
        assert rainfall.end_year == 1910

    def test_get_month(self):
        rainfall = Rainfall()

        with tempfile.TemporaryDirectory() as tmpdirname:
            rainfall.fetch_data_years(1901, 1910, extract_to=tmpdirname)
        
        res = rainfall.get_month(5, 1902)
        assert res.shape[0] == 360
        assert res.shape[1] == 720
