class Solution(object):
# Brute force version, so it time fails
  
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        max_speed = max(piles)
        for speed in range(1, max_speed + 1):
            hours = 0 
            for pile in piles:
                while pile > 0:
                    pile -= speed
                    hours += 1
            if hours <= h:
                return speed
        return max_speed
                
