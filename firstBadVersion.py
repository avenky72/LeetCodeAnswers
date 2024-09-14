# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        earliest = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid) == True:
                earliest = mid
                right = mid
            else:
                left = mid + 1
        return earliest
        
