# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1

        most = 0
        while j > i:
            temp_area = min(height[i], height[j]) * (j-i)
            print(temp_area, i, j)
            if temp_area > most:
                most = temp_area
            if height[i] >= height[j]:
                j -= 1
            elif height[j] > height[i]:
                i+= 1 
        return most
            
