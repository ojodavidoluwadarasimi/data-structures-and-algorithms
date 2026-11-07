"""
Problem: Find the first index of a target value in a list.

Approach: Check each item from left to right. Return the index as soon as
the target is found. If the loop finishes without a match, return -1.

Time complexity:
- Best case: O(1), when the first item matches.
- Average case: O(n), where n is the number of items.
- Worst case: O(n), when the target is last or absent.

Space complexity: O(1), because the algorithm uses a fixed amount of
additional memory.
"""


def linear_search(items: list[int], target: int) -> int:
    """Return the first index of target in items, or -1 if it is absent."""
    for index, item in enumerate(items):
        if item == target:
            return index

    return -1


if __name__ == "__main__":
    numbers = [12, 7, 19, 3, 25, 7]

    # Target at the beginning, middle, and end.
    assert linear_search(numbers, 12) == 0
    assert linear_search(numbers, 19) == 2
    assert linear_search(numbers, 7) == 1  # First occurrence is returned.
    assert linear_search(numbers, 7) == 1
    assert linear_search(numbers, 7) == 1

    # Target is absent.
    assert linear_search(numbers, 100) == -1

    # Edge cases.
    assert linear_search([], 5) == -1
    assert linear_search([42], 42) == 0
    assert linear_search([42], 10) == -1

    print("linear_search: all tests passed")
