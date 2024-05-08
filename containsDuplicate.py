# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
 
        Using Array
        counter = []
        for i in nums:
            if i not in counter:
                counter.append(i)
            elif i in counter:
                return True
        print(counter)
        return False
        """
        
        # Using Sorting
        nums.sort()
        for i in range(0, len(nums)-1):
            if (nums[i] == nums[i+1]):
                return True
        return False

