# test_bubble_sort.py

from ..bubble_sort import bubble_sort

import pytest

def test_bubble_sort():
    # Test 1: Normal list
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4], "Should sort a list in ascending order"

    # Test 2: List with duplicate elements
    assert bubble_sort([3, 2, 1, 2]) == [1, 2, 2, 3], "Should handle duplicate elements"
    
    # Test 3: List with negative numbers
    assert bubble_sort([-2, -1, -3, -4]) == [-4, -3, -2, -1], "Should handle negative numbers"    

    # Test 4: Single-element list
    assert bubble_sort([1]) == [1], "Should handle single-element list"
    
    # Test 5: Empty list
    assert bubble_sort([]) == [], "Should handle empty list"
    
    # Test 6: Already sorted list
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4], "Should handle already sorted list"
    
    # Test 7: Reverse sorted list
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4], "Should handle reverse sorted list"
    
    # Error handling
    with pytest.raises(TypeError):
        bubble_sort(5, 4, 3, 2, 1)
    
    with pytest.raises(TypeError):
        bubble_sort("This is not a list")

    with pytest.raises(TypeError):
        bubble_sort({5: 4, 3: 2, 1: 0})
