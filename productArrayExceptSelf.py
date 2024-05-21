class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = list(nums)

        for i in range(len(nums)):
            k = 1
            for j in range(len(nums)):
                if j == i:
                    j += 1
                else:
                    k = k * nums[j]
            nums2[i] = k
        return(nums2)
