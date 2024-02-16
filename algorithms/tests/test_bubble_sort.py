# test_bubble_sort.py

import pytest
from ..bubble_sort import bubble_sort

@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        # Test 1: Normal list
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        # Test 2: List with duplicate elements
        ([3, 2, 1, 2], [1, 2, 2, 3]),
        # Test 3: List with negative numbers
        ([-2, -1, -3, -4], [-4, -3, -2, -1]),
        # Test 4: Single-element list
        ([1], [1]),
        # Test 5: Empty list
        ([], []),
        # Test 6: Already sorted list
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        # Test 7: Reverse sorted list
        ([4, 3, 2, 1], [1, 2, 3, 4]),
    ],
)
def test_bubble_sort(input_list, expected_output):
    assert bubble_sort(input_list) == expected_output

@pytest.mark.parametrize(
    "input_list",
    [
        # Test 1: Non-list input (tuple)
        (5, 4, 3, 2, 1),
        # Test 2: Non-list input (string)
        "This is not a list",
        # Test 3: Non-list input (dictionary)
        {5: 4, 3: 2, 1: 0},
    ],
)
def test_bubble_sort_errors(input_list):
    with pytest.raises(TypeError):
        bubble_sort(input_list)