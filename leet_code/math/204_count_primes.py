import math


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Counts the number of prime numbers less than a non-negative number, n.

        Args:
            n: The upper limit (exclusive).

        Returns:
            The number of prime numbers less than n.
        """
        if n < 2:  # 0 and 1 are not prime
            return 0

        is_prime = [
            1
        ] * n  # Initialize a list to store primality flags (1 for prime, 0 for not prime)
        is_prime[0] = is_prime[1] = 0  # Mark 0 and 1 as not prime

        # Iterate up to the square root of n.  Any number greater than sqrt(n)
        # that is not prime will have a factor less than or equal to its square root.
        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if is_prime[i]:  # If i is prime...
                # Mark all multiples of i (starting from i*i) as not prime.
                # We start from i*i because any smaller multiple would have been
                # marked as not prime by a smaller prime number already.
                # We increment by i to efficiently cover all multiples.
                for multiple_of_i in range(i**2, n, i):
                    is_prime[multiple_of_i] = 0

        return sum(
            is_prime
        )  # Return the count of prime numbers (sum of all True values in is_prime list)


# Test cases
solution = Solution()

# Test case 1: n = 10
n1 = 10
expected1 = 4  # Primes: 2, 3, 5, 7
result1 = solution.countPrimes(n1)
print(f"Test case 1: Expected: {expected1}, Got: {result1}")
assert result1 == expected1


# Test case 2: n = 0
n2 = 0
expected2 = 0
result2 = solution.countPrimes(n2)
print(f"Test case 2: Expected: {expected2}, Got: {result2}")
assert result2 == expected2

# Test case 3: n = 1
n3 = 1
expected3 = 0
result3 = solution.countPrimes(n3)
print(f"Test case 3: Expected: {expected3}, Got: {result3}")
assert result3 == expected3


# Test case 4: n = 2
n4 = 2
expected4 = 0
result4 = solution.countPrimes(n4)
print(f"Test case 4: Expected: {expected4}, Got: {result4}")
assert result4 == expected4

# Test case 5: n = 3
n5 = 3
expected5 = 1  # Prime: 2
result5 = solution.countPrimes(n5)
print(f"Test case 5: Expected: {expected5}, Got: {result5}")
assert result5 == expected5

# Test case 6: Larger number
n6 = 50
expected6 = 15  # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
result6 = solution.countPrimes(n6)
print(f"Test case 6: Expected: {expected6}, Got: {result6}")
assert result6 == expected6
