class Solution:
    def jump(self, nums: List[int]) -> int:
        curr = 0 
        count = 0
        while curr < len(nums) - 1:
            longest = curr
            index = 0

            for i in range(1, nums[curr]+1): 
                jump = curr + i + nums[curr+i]
                
                if curr + i >= len(nums) - 1:
                    count += 1
                    return count

                if jump > longest:
                    longest = jump
                    index = i

            curr += index
            count += 1
        return count
                
                
