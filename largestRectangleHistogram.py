class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        max_area = 0
        stack = [] # (index, height)

        for i in range(n):
            curr = heights[i]
            while stack and curr < stack[-1][1]:
                index, height = stack.pop()
                width = i if not stack else i - stack[-1][0] - 1
                max_area = max(max_area, (height * width))
            stack.append((i, curr))
        
        while stack:
            i, h = stack.pop()
            width = n if not stack else n - stack[-1][0] - 1
            max_area = max(max_area, h * width)
        
        return max_area



"""
        n = len(heights)
        max_area = 0  # To track the maximum area found
        
        for i in range(n):
            min_height = heights[i]  # Start with the current bar's height
            
            for j in range(i, n):
                # Update the minimum height in the stretch
                min_height = min(min_height, heights[j])
                
                # Calculate the area of the rectangle
                width = j - i + 1
                area = min_height * width
                
                # Update the maximum area
                max_area = max(max_area, area)
        
        return max_area
"""
