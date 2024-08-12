class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ start and take the greedy approach:
        at an index, loop through all the possibilities and pick 
        the one that has the largest reach
        continue until the end

        or start from the end and keep a pointer
        if an index can reach the end pointer, update the pointer
        to that index and repeat until you reach the start """

        curr = 0  
        while curr < len(nums) - 1: 
            print("curr index: ", curr, " value: ", nums[curr])
            if nums[curr] == 0:
                return False
            
            longest = curr
            index = 0

            for i in range(1, nums[curr] + 1):
                if curr + i >= len(nums) - 1:
                    return True
                
                jump = nums[curr+i] + i + curr
                if jump > longest:
                    longest = jump
                    index = i
                
            if index == 0:
                return False

            curr += index
            
        return True
