import math


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        def distance(x, y):
            return math.sqrt((x ** 2) + (y ** 2))

        result = {}

        for i in points:
            distances = [(i, distance(i[0], i[1])) for i in points]
            sorted_distances = sorted(distances, key=lambda x: x[1])
            closest_k = [i[0] for i in sorted_distances[:k]]
            return closest_k




points = [[3,3],[5,-1],[-2,4]]
k = 2

