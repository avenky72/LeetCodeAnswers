class Solution(object):
# Return the maximum product difference between two pairs
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            if i > a:
                a = i

        for i in nums:
            if i == a:
                nums.remove(i)

        b = 0
        for i in nums:
            if i > b:
                b = i

        c = a
        for i in nums:
            if i < c:
                c = i

        for i in nums:
            if i == c:
                nums.remove(c)
        d = a
        for i in nums:
            if i < d:
                d = i

        return ((a*b) - (c*d))

        
