class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        for i in nums:
            if i in visited:
                return i
            else:
                visited.add(i)
