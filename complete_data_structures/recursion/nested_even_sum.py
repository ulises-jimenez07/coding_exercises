#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# nestedEvenSum Solution

obj1 = {"outer": 2, "obj": {"inner": 2, "otherObj": {"superInner": 2, "notANumber": True, "alsoNotANumber": "yup"}}}

obj2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": "ball", "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": "car"},
}


def nestedEvenSum(obj, total=0):
    """Recursively sums even numbers in a nested dictionary."""
    for key in obj:
        if isinstance(obj[key], dict):
            total += nestedEvenSum(obj[key])
        elif isinstance(obj[key], int) and obj[key] % 2 == 0:
            total += obj[key]
    return total
