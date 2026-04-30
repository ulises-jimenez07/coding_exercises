"""
Problem: K-Means Clustering
Group points into k clusters by repeatedly assigning points to the nearest centroid.

Approach:
- Pick k initial centroids from the data
- Assign each point to its nearest centroid
- Replace each centroid with the mean of its assigned points
- Stop when centroids no longer move or max iterations is reached
- Time complexity: O(iterations * n * k * d)
- Space complexity: O(n + k)
"""

import math
import random
import unittest


class KMeans:
    """Basic k-means clustering implementation."""

    def __init__(self, k=3, max_iters=100, random_state=None):
        if k < 1:
            raise ValueError("k must be at least 1")
        if max_iters < 1:
            raise ValueError("max_iters must be at least 1")

        self.k = k
        self.max_iters = max_iters
        self.random_state = random_state
        self.centroids = []

    def _distance(self, first_point, second_point):
        """Return Euclidean distance between two points."""
        return math.sqrt(sum((first_point[i] - second_point[i]) ** 2 for i in range(len(first_point))))

    def _mean_point(self, cluster):
        """Return the arithmetic mean point for a cluster."""
        dimensions = len(cluster[0])
        return [sum(point[i] for point in cluster) / len(cluster) for i in range(dimensions)]

    def fit(self, data):
        """Fit centroids to data and return final centroid positions."""
        if self.k > len(data):
            raise ValueError("k cannot be greater than the number of data points")

        self.centroids = [list(point) for point in random.Random(self.random_state).sample(data, self.k)]

        for _ in range(self.max_iters):
            clusters = [[] for _ in range(self.k)]

            for point in data:
                distances = [self._distance(point, centroid) for centroid in self.centroids]
                closest_index = distances.index(min(distances))
                clusters[closest_index].append(point)

            new_centroids = []
            for index, cluster in enumerate(clusters):
                if cluster:
                    new_centroids.append(self._mean_point(cluster))
                else:
                    new_centroids.append(self.centroids[index])

            if new_centroids == self.centroids:
                break
            self.centroids = new_centroids

        return self.centroids

    def predict(self, point):
        """Return the nearest centroid index for a point after fitting."""
        if not self.centroids:
            raise ValueError("model must be fit before calling predict")

        distances = [self._distance(point, centroid) for centroid in self.centroids]
        return distances.index(min(distances))


class TestKMeans(unittest.TestCase):
    """Unit tests for KMeans."""

    def test_fit_two_clusters(self):
        data = [
            [0.0, 0.0],
            [0.0, 1.0],
            [10.0, 10.0],
            [10.0, 11.0],
        ]
        model = KMeans(k=2, max_iters=20, random_state=1)
        centroids = sorted(model.fit(data))

        self.assertEqual(centroids, [[0.0, 0.5], [10.0, 10.5]])

    def test_predict_after_fit(self):
        data = [
            [0.0, 0.0],
            [1.0, 0.0],
            [9.0, 9.0],
            [10.0, 9.0],
        ]
        model = KMeans(k=2, max_iters=20, random_state=3)
        model.fit(data)
        low_cluster = model.predict([0.0, 0.5])
        high_cluster = model.predict([10.0, 10.0])

        self.assertNotEqual(low_cluster, high_cluster)

    def test_invalid_k(self):
        with self.assertRaises(ValueError):
            KMeans(k=0)

    def test_more_clusters_than_points(self):
        model = KMeans(k=3)

        with self.assertRaises(ValueError):
            model.fit([[1.0, 2.0], [3.0, 4.0]])

    def test_predict_before_fit(self):
        model = KMeans(k=1)

        with self.assertRaises(ValueError):
            model.predict([1.0, 2.0])


if __name__ == "__main__":
    unittest.main()
