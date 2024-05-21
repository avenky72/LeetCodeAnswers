class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        num = set(sorted(nums))
        print num
        length = 0
        count = 0
        
        for i in num:
            if (i-1) not in num:
                length = max(count, length)
                count = 1
                while (i+1) in num:
                    count += 1
                    i+=1
        length = max(count, length)
        return length
