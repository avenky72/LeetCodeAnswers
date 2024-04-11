# Remove duplicate values in an array, without using any remove/pop/etc functions
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = set(nums)
        k = len(num)
        j = 1

        while j < k:
            for i in range(len(nums)-1):
                # if the next element isn't equal to the current element (unique so far)
                if nums[i] != nums[i+1]:
                    # set that new value to the jth index in the array
                    nums[j] = nums[i+1]
                    j += 1
        return k
