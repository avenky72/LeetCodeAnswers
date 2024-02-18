class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = 0
        maxj = 0
        max = 0
        total = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if (nums[i]*nums[j]) > max:
                        max = (nums[i]*nums[j])
                        maxj = nums[j]
                        maxi = nums[i]
        maxi -= 1
        maxj -= 1
        total = maxi*maxj
        return total
