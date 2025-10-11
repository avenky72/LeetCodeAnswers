class Solution:
    def rob(self, nums: List[int]) -> int:

        size = len(nums)

        if size > 2:

            cache = [0] * size
            
            cache[size-1] = nums[size-1]
            cache[size-2] = max(nums[size-2], nums[size-1])


            for i in range(len(cache)-3, -1, -1):
                cache[i] = max((nums[i]+cache[i+2]), cache[i+1])
            print(cache)
            
            return cache[0]
        
        if size == 2:
            return max(nums[0], nums[1])

        if size == 1:
            return nums[0]
