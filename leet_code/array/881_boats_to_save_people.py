class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        Calculates the minimum number of boats needed to save people, given their weights and a boat's weight limit.

        Each boat can carry at most two people at the same time, provided the sum of the people's weights is at most limit.

        :type people: List[int]  # List of people's weights
        :type limit: int        # The boat's weight limit
        :rtype: int           # The minimum number of boats needed
        """
        people.sort()  # Sort people by weight to optimize pairing

        smallest = 0  # Pointer to the lightest person
        biggest = len(people) - 1  # Pointer to the heaviest person
        boats = 0  # Counter for the number of boats

        while biggest >= smallest:  # Continue until all people are considered
            # If the heaviest and lightest person can fit in a boat together...
            if people[biggest] + people[smallest] <= limit:
                biggest -= 1  # Heaviest person gets on the boat
                smallest += 1  # Lightest person gets on the same boat
            # Otherwise, the heaviest person needs a boat alone
            else:
                biggest -= 1  # Heaviest person takes a boat alone
            boats += 1  # Increment boat count in both cases

        return boats  # Return the total number of boats needed


# Test cases
solution = Solution()

# Test case 1: Basic example
people1 = [1, 2, 2, 3]
limit1 = 3
expected1 = 3
result1 = solution.numRescueBoats(people1, limit1)
print(f"Test case 1: Expected {expected1}, Got {result1}")
assert result1 == expected1

# Test case 2: Everyone can fit in pairs
people2 = [2, 3, 3, 4]
limit2 = 5
expected2 = 3
result2 = solution.numRescueBoats(people2, limit2)
print(f"Test case 2: Expected {expected2}, Got {result2}")
assert result2 == expected2

# Test case 3:  Heaviest person exceeds the limit
people3 = [5, 1, 4, 2]
limit3 = 6
expected3 = 2
result3 = solution.numRescueBoats(people3, limit3)
print(f"Test case 3: Expected {expected3}, Got {result3}")
assert result3 == expected3

# Test case 4: All people have same weight, pairs can be formed
people4 = [3, 3, 3, 3]
limit4 = 6
expected4 = 2
result4 = solution.numRescueBoats(people4, limit4)
print(f"Test case 4: Expected {expected4}, Got {result4}")
assert result4 == expected4


# Test case 5: Empty list
people5 = [list]
limit5 = 5
expected5 = 0
result5 = solution.numRescueBoats(people5, limit5)
print(f"Test case 5: Expected {expected5}, Got {result5}")
assert result5 == expected5

# Test case 6: Single person
people6 = [7]
limit6 = 8
expected6 = 1
result6 = solution.numRescueBoats(people6, limit6)
print(f"Test case 6: Expected {expected6}, Got {result6}")
assert result6 == expected6
