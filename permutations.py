class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        output = []
        perm = []
        values = nums[:]


        def permutation():
            if len(perm) == len(nums):
                output.append(perm[:])
                return
            
            for i in values:
                if i not in perm:
                    perm.append(i)
                    #values.remove(i)
                    permutation()
                    perm.remove(i)
                    #values.append(i)
                    #print(values)
        
        permutation()
        print(output)
        return output
