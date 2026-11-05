"""
Problem: Sort a list of numbers from smallest to largest.

Approach: Go through the list and swap neighbouring items that are in the
wrong order. After each full pass the largest remaining item has "bubbled"
to the end. If a pass makes no swaps, the list is already sorted and we stop.

Time complexity:  O(n^2) worst and average case, O(n) if already sorted
Space complexity: O(1)   (sorts in place)
"""


def bubble_sort(items: list[int]) -> list[int]:
    data = items.copy()  # keep the original list unchanged
    n = len(data)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break

    return data


if __name__ == "__main__":
    assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    print("bubble_sort: all tests passed")
