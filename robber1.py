class Solution:
    def rob(self, nums: List[int]) -> int:
        output = len(nums) * [0]
        output[0] = nums[0]
         
        if len(nums) > 1:
            output[1] = max(nums[1], nums[0])

            for i in range(2, len(nums)):
                output[i] = max(output[i-1], (output[i-2] + nums[i]))
                print(output)
            return output[len(nums)-1]
        else:
            return nums[0]
