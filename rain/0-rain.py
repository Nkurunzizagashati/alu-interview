#!/usr/bin/python3
"""calculate how many square units of
water will be retained after it rains
"""


def rain(walls):
    """
    this function calculates how many square units of
    water will be retained after it rains
    """
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    max_left, max_right = 0, 0
    water = 0

    while left <= right:
        if walls[left] <= walls[right]:
            max_left = max(max_left, walls[left])
            water += max_left - walls[left]
            left += 1
        else:
            max_right = max(max_right, walls[right])
            water += max_right - walls[right]
            right -= 1

    return water
