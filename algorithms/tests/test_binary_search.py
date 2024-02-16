# test_binary_search.py

import pytest
from ..binary_search import binary_search

@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Test 1: Target is in the list
        ([1,2,3,4,5], 3, 2),
        # Test 2: Target is the first element
        ([1, 2, 3, 4, 5], 1, 0),
        # Test 3: Target is the last element
        ([1, 2, 3, 4, 5], 5, 4),
        # Test 4: Target is not in the list
        ([1, 2, 3, 4, 5], 6, -1),
        # Test 5: Empty list
        ([], 1, -1),
        # Test 6: Single-element list, target is present
        ([1], 1, 0),
        # Test 7: Single-element list, target is absent
        ([1], 2, -1),
        # Test with duplicate elements
        ([1, 2, 2, 3, 4, 5], 2, 2),
        # Test with negative numbers
        ([-3, -2, -1, 0, 1, 2, 3], -1, 2),
    ]
)
def test_binary_search(nums, target, expected):
    assert binary_search(nums, target) == expected

def test_binary_search_errors_and_edge_cases():
        # Test with unsorted list
    with pytest.raises(ValueError):
        binary_search([5, 2, 3, 1, 4], 3)

    # Test with large list
    assert binary_search(list(range(1, 1000001)), 999999) == 999998

    # Test with different data types
    assert binary_search(['apple', 'banana', 'cherry', 'date'], 'cherry') == 2

    # Error handling
    with pytest.raises(TypeError):
        binary_search(123, 1)

    with pytest.raises(TypeError):
        binary_search(['apple', 'banana', 3, 'date'], 'cherry')
