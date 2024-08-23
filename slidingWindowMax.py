class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        max_index = None
        output = []

        # First iteration of window and it's max + index
        big = max(nums[left:k])
        index = nums[left:k].index(big)
        max_index = left + index
        output.append(big)

        for right in range(k, len(nums)):
            left += 1
            if max_index >= left:
                big = max(big, nums[right])
                if big == nums[right]:
                    max_index = right
                output.append(big)
            else:
                big = max(nums[left:right+1])
                index = nums[left:right+1].index(big)
                max_index = left + index
                output.append(big)

        return output

        
