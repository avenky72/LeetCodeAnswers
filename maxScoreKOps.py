class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        for i in range(k):
            op = max(nums)
            score += op
            nums[nums.index(op)] = int(math.ceil(nums[nums.index(op)]/3))
        return score
