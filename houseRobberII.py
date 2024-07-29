class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def robberDP(houses):


            for i in range(len(houses)):
                if i == 0:
                    houses[0] = houses[0]
                elif i == 1:
                    houses[1] = max(houses[1], houses[0])
                else:
                    houses[i] = max(houses[i-1], (houses[i]+houses[i-2]))

            return houses[-1]

        nums1 = nums[:-1] 
        nums2 = nums[1:] 
        return max(robberDP(nums1[:]), robberDP(nums2[:]))

        



            

        
