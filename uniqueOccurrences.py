# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}
        for i in arr:
            dict[i] = dict.get(i, 0) + 1

        lst = []
        for j in dict.values():
            if j in lst:
                return False
            lst.append(j)
        return True
