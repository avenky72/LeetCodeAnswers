class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            #temp = nums[m]
            
            # if nums[r] < nums[m] the min is in the right if nums[r] > nums[m] the min is in the left
            if nums[r] < nums[m]:
                l = m + 1

            elif nums[r] > nums[m]:
                r = m

        # used code from min in rotated arry probelm   
        min = l
        
        temp = nums[min:] + nums[:min]
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if temp[m] == target:
                print(temp[m])
                # after finding the value in the unrotated array, find its index in the original array
                return (m + min) % len(nums)
            elif temp[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1


        
