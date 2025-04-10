import sys

sys.path.insert(0, '.')
sys.path.insert(1, '..')

from fetch_rainfall import fetch_rainfall

class TestFetchRainfall:
    def test_fetch_1(self):
        test = fetch_rainfall(['Syria'], ['SYR'])
        assert len(test) != 0