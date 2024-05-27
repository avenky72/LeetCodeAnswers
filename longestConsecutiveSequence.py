class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums = list(set(nums))
        nums.sort()
        count = 1
        longest = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 1
        return longest
