"""
Problem: K-Fold Cross Validation
Split data indices into k folds for repeated train/test validation.

Approach:
- Create a list of indices for the input data
- Optionally shuffle the indices
- Divide indices into k folds as evenly as possible
- Yield each fold once as test indices and all remaining folds as train indices
- Time complexity: O(n * k) for producing all splits
- Space complexity: O(n)
"""

import random
import unittest


class KFold:
    """Simple k-fold index splitter."""

    def __init__(self, k=5, shuffle=True, random_state=None):
        if k < 2:
            raise ValueError("k must be at least 2")

        self.k = k
        self.shuffle = shuffle
        self.random_state = random_state

    def split(self, data):
        """Yield (train_indices, test_indices) tuples."""
        if self.k > len(data):
            raise ValueError("k cannot be greater than the number of data points")

        indices = list(range(len(data)))
        if self.shuffle:
            random.Random(self.random_state).shuffle(indices)

        base_size, extra = divmod(len(data), self.k)
        folds = []
        start = 0

        for fold_index in range(self.k):
            fold_size = base_size + (1 if fold_index < extra else 0)
            end = start + fold_size
            folds.append(indices[start:end])
            start = end

        for fold_index in range(self.k):
            test_indices = folds[fold_index]
            train_indices = []
            for other_index, fold in enumerate(folds):
                if other_index != fold_index:
                    train_indices.extend(fold)
            yield train_indices, test_indices


class TestKFold(unittest.TestCase):
    """Unit tests for KFold."""

    def test_split_without_shuffle(self):
        data = ["a", "b", "c", "d", "e"]
        folds = list(KFold(k=2, shuffle=False).split(data))

        self.assertEqual(folds[0], ([3, 4], [0, 1, 2]))
        self.assertEqual(folds[1], ([0, 1, 2], [3, 4]))

    def test_every_index_appears_once_as_test(self):
        data = list(range(10))
        folds = list(KFold(k=5, shuffle=False).split(data))
        test_indices = [index for _, test_fold in folds for index in test_fold]

        self.assertEqual(sorted(test_indices), list(range(10)))

    def test_shuffle_is_deterministic_with_seed(self):
        data = list(range(8))
        first = list(KFold(k=4, shuffle=True, random_state=7).split(data))
        second = list(KFold(k=4, shuffle=True, random_state=7).split(data))

        self.assertEqual(first, second)

    def test_invalid_k(self):
        with self.assertRaises(ValueError):
            KFold(k=1)

    def test_too_many_folds(self):
        with self.assertRaises(ValueError):
            list(KFold(k=4).split([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
