def add_binary(a, b):
    """
    Adds two binary strings and returns their sum as a binary string.

    Args:
        a: The first binary string.
        b: The second binary string.

    Returns:
        The sum of a and b as a binary string.
    """
    i = len(a) - 1  # Pointer for string a
    j = len(b) - 1  # Pointer for string b
    carry = 0  # Initialize carry
    res = ""  # Initialize result string

    # Iterate while there are digits remaining or a carry
    while i >= 0 or j >= 0 or carry > 0:
        if i >= 0:
            carry += int(a[i])  # Add digit from a to carry
            i -= 1
        if j >= 0:
            carry += int(b[j])  # Add digit from b to carry
            j -= 1

        res = str(carry % 2) + res  # Append the sum's digit to the result
        carry = carry // 2  # Update the carry

    return res


# Test cases
def test_add_binary():
    # Test case 1: Basic example
    a1 = "11"
    b1 = "1"
    expected1 = "100"
    assert (
        add_binary(a1, b1) == expected1
    ), f"Test case 1 failed: Expected {expected1}, got {add_binary(a1, b1)}"

    # Test case 2: Longer strings
    a2 = "1010"
    b2 = "1011"
    expected2 = "10101"
    assert (
        add_binary(a2, b2) == expected2
    ), f"Test case 2 failed: Expected {expected2}, got {add_binary(a2, b2)}"

    # Test case 3: Strings of different lengths
    a3 = "111"
    b3 = "1"
    expected3 = "1000"
    assert (
        add_binary(a3, b3) == expected3
    ), f"Test case 3 failed: Expected {expected3}, got {add_binary(a3, b3)}"

    # Test case 4: One string is empty
    a4 = "11"
    b4 = ""
    expected4 = "11"
    assert (
        add_binary(a4, b4) == expected4
    ), f"Test case 4 failed: Expected {expected4}, got {add_binary(a4, b4)}"

    # Test case 5: Both strings are empty
    a5 = ""
    b5 = ""
    expected5 = ""
    assert (
        add_binary(a5, b5) == expected5
    ), f"Test case 5 failed: Expected {expected5}, got {add_binary(a5, b5)}"

    print("All test cases passed!")


test_add_binary()
