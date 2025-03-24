
import pytest
import sys

sys.path.insert(0, '.')
sys.path.insert(1, '..')


import numpy as np

from utils import diff

class TestDiff:
    def test_simple(self):
        arr = np.array([1, 2, 3, 4, 5])
        res = diff(arr)
        assert len(res) == len(arr) - 1

    def test_2(self):
        arr = np.array([1, 1, 1, 1, 1])
        res = diff(arr)

        assert len(res) == len(arr) - 1

        assert np.all(np.isclose(res, 0)) 

    def test_with_lag(self):
        arr = np.array([1, 2, 3, 4, 5])
        res_0 = diff(arr)
        res = diff(arr, lag=1)

        assert len(res) == len(arr) - 2
        assert np.all(np.isclose(res_0[:-1], res))

    def test_large_lag(self):
        arr = np.ones(10)

        with pytest.raises(ValueError):
            res = diff(arr, lag=15)