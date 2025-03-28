"""
Rainfall and World classes to fetch and analyze rainfall data.

To be reorganized/refactored as part of the larger code as we merge things together.

By Irem Altan.
"""

from statistics import mean
import os
import cv2
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

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
    
