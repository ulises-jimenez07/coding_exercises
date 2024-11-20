class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Determines if a robot returns to the origin after a sequence of moves.

        The robot moves on a plane starting from the origin (0, 0). "U" moves the robot up one unit, "D" moves it down one unit, "L" moves it left one unit, and "R" moves it right one unit. The function checks if the robot returns to the origin after it finishes all of its moves.

        Args:
            moves: A string consisting of 'U', 'D', 'L', and 'R' characters representing the robot's moves.

        Returns:
            True if the robot returns to the origin, False otherwise.
        """
        x = 0  # Represents the horizontal position (positive right, negative left)
        y = 0  # Represents the vertical position (positive up, negative down)

        for move in moves:  # Iterate through each move
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
            elif move == "R":
                x += 1

        return x == 0 and y == 0  # Return True if both x and y are 0 (back at origin)


# Test cases
solution = Solution()

# Test case 1: Returns to origin
moves1 = "UD"
expected1 = True
assert (
    solution.judgeCircle(moves1) == expected1
), f"Test case 1 failed. Expected {expected1}, got {solution.judgeCircle(moves1)}"

# Test case 2: Returns to origin (longer sequence)
moves2 = "LDRRLRUULR"
expected2 = False
assert (
    solution.judgeCircle(moves2) == expected2
), f"Test case 2 failed. Expected {expected2}, got {solution.judgeCircle(moves2)}"

# Test case 3: Does not return to origin
moves3 = "LL"
expected3 = False
assert (
    solution.judgeCircle(moves3) == expected3
), f"Test case 3 failed. Expected {expected3}, got {solution.judgeCircle(moves3)}"


# Test case 4: Empty moves
moves4 = ""
expected4 = True
assert (
    solution.judgeCircle(moves4) == expected4
), f"Test case 4 failed. Expected {expected4}, got {solution.judgeCircle(moves4)}"

# Test case 5: Circular movement
moves5 = "ULDR"
expected5 = True
assert (
    solution.judgeCircle(moves5) == expected5
), f"Test case 5 failed. Expected {expected5}, got {solution.judgeCircle(moves5)}"

print("All test cases passed!")
