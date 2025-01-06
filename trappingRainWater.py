class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        n = len(height)
        area = 0
        max_left = [0] * n
        max_right = [0] * n

        # First and last elements
        max_left[0] = height[0]
        max_right[n-1] = height[n-1]

        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])

        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        for i in range(n):
            area += max(min(max_left[i], max_right[i]) - height[i], 0)

        return area
        



        """
        area = 0
        rain = [] # (max left, max right)
        for i in range(len(height)):
            if i == 0:
                rain.append((height[0], max(height[1:])))
            elif i == len(height)-1:
                rain.append((max(height[:i]), height[i]))
            else:
                rain.append((max(height[:i]), max(height[i+1:])))
            area += max(min(rain[i][0], rain[i][1]) - height[i], 0)
        
        return area
        """
