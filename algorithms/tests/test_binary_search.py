# test_binary_search.py

import pytest

from ..binary_search import binary_search

def test_binary_search():
    # Test 1: Target is in the list
    assert binary_search([1,2,3,4,5], 3) == 2, "Should return the index of 3"

    # Test 2: Target is the first element
    assert binary_search([1, 2, 3, 4, 5], 1) == 0, "Should return the index of 1"

    # Test 3: Target is the last element
    assert binary_search([1, 2, 3, 4, 5], 5) == 4, "Should return the index of 5"

    # Test 4: Target is not in the list
    assert binary_search([1, 2, 3, 4, 5], 6) == -1, "Should return -1 for a missing element"

    # Test 5: Empty list
    assert binary_search([], 1) == -1, "Should return -1 for an empty list"

    # Test 6: Single-element list, target is present
    assert binary_search([1], 1) == 0, "Should return 0 for a single-element list where the target is present"

    # Test 7: Single-element list, target is absent
    assert binary_search([1], 2) == -1, "Should return -1 for a single-element list where the target is absent"

    # Test with unsorted list
    with pytest.raises(ValueError):
        binary_search([5, 2, 3, 1, 4], 3)

    # Test with duplicate elements
    assert binary_search([1, 2, 2, 3, 4, 5], 2) in [1, 2]

    # Test with negative numbers
    assert binary_search([-3, -2, -1, 0, 1, 2, 3], -1) == 2

    # Test with large list
    assert binary_search(list(range(1, 1000001)), 999999) == 999998

    # Test with different data types
    assert binary_search(['apple', 'banana', 'cherry', 'date'], 'cherry') == 2

    # Error handling
    with pytest.raises(TypeError):
        binary_search(123, 1)

    with pytest.raises(TypeError):
        binary_search(['apple', 'banana', 3, 'date'], 'cherry')

if __name__ == "__main__":
    test_binary_search()