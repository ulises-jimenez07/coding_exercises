from typing import List
import unittest

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Finds the next greater element for each element in the input list,
        considering the list as circular.

        Args:
            nums: A list of integers.

        Returns:
            A list of integers where each element is the next greater element
            for the corresponding element in `nums`. If there is no greater
            element, the value is -1.
        """
        stack = []  # Stack to store indices of elements
        stack.append(0)  # Initialize stack with the index of the first element

        n = len(nums)
        ans = [-1] * n  # Initialize the result list with -1

        # First pass: Iterate through the array once
        for i in range(1, n):
            current = nums[i]
            # While the stack is not empty and the current element is greater
            # than the element at the index stored at the top of the stack
            while len(stack) > 0 and nums[stack[-1]] < current:
                ans[stack[-1]] = current  # Update the result for the top of the stack
                stack.pop()  # Remove the top element from the stack
            stack.append(i)  # Push the current element's index onto the stack

        # Second pass: Iterate through the array again to handle the circularity
        for i in range(0, n):
            current = nums[i]
            # Similar logic as in the first pass
            while len(stack) > 0 and nums[stack[-1]] < current:
                ans[stack[-1]] = current
                stack.pop()
        
        return ans

class TestNextGreaterElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Solution().nextGreaterElements([]), [])

    def test_single_element_list(self):
        self.assertEqual(Solution().nextGreaterElements([1]), [-1])

    def test_example_1(self):
        self.assertEqual(Solution().nextGreaterElements([1, 2, 1]), [2, -1, 2])

    def test_example_2(self):
        self.assertEqual(Solution().nextGreaterElements([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4])

    def test_decreasing_list(self):
        self.assertEqual(Solution().nextGreaterElements([4, 3, 2, 1]), [-1, 4, 4, 4])

    def test_increasing_list(self):
        self.assertEqual(Solution().nextGreaterElements([1, 2, 3, 4]), [2, 3, 4, -1])

    def test_circular_example_1(self):
        self.assertEqual(Solution().nextGreaterElements([5,4,3,2,1]), [-1, 5, 5, 5, 5])
    
    def test_circular_example_2(self):
        self.assertEqual(Solution().nextGreaterElements([1,5,3,6,8]), [5, 6, 6, 8, -1])

if __name__ == '__main__':
    unittest.main()
