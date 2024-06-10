class Solution(object):
# Binary Search Version
  
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        right = max(piles)
        left = 1
        
        while right >= left:
            speed = (left + right) // 2
            hours = 0 
            for pile in piles:
                hours += (pile + speed - 1) // speed  
                """
                Same as
                for pile in piles:
                while pile > 0:
                    pile -= speed
                    hours += 1
                But more efficient 
                """
            if hours > h:
                left = speed + 1
            else:
                right = speed - 1
        
        return left
