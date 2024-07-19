class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        sub = []

        n = len(nums)

        def subset(i = 0):
            if i == n:
                output.append(sub[:])
                return
            
            subset(i+1)
            sub.append(nums[i])
            subset(i+1)
            #sub.remove(i+1)
            sub.pop()
        
        subset()
        return output


