class Solution(object):
# Given an integer n, return true if it is a power of four. Otherwise, return false.
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p4 = True
        if n == 1:
            return True
        if n == 0: 
            return False
        if n % 4 == 0:
            return self.isPowerOfFour(n/4)
        else:
            return False
