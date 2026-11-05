"""
Problem: Find the index of a target value in a sorted list.
Return -1 if the target is not in the list.

Approach: Compare the target with the middle element. If it matches, return
the index. If the target is smaller, search the left half. If it is larger,
search the right half. Repeat until the search range is empty.

Time complexity:  O(log n)  (the search range halves every step)
Space complexity: O(1)      (only a few index variables)
"""


def binary_search(items: list[int], target: int) -> int:
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11]
    assert binary_search(numbers, 7) == 3
    assert binary_search(numbers, 1) == 0
    assert binary_search(numbers, 11) == 5
    assert binary_search(numbers, 4) == -1
    assert binary_search([], 4) == -1
    print("binary_search: all tests passed")
