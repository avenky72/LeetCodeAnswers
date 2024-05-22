class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distance = {}
        output = []

        for i in points:
            dist = (i[0]**2) + (i[1]**2)
            distance[tuple(i)] = dist
        values = sorted(distance.items(), key=lambda x: x[1])
        for j in values[:k]:
            l = list(j[0])
            output.append(l)
        return output


      
