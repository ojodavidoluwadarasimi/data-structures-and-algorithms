"""
Problem: Reverse a string.

Approach: Walk through the string from the last character to the first
and build the result in a list, then join it into one string.

Time complexity:  O(n)  (visits each character once)
Space complexity: O(n)  (stores the reversed characters)
"""


def reverse_string(text: str) -> str:
    result = []
    for i in range(len(text) - 1, -1, -1):
        result.append(text[i])
    return "".join(result)


if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    print("reverse_string: all tests passed")
