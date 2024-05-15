# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        combinations = []
        for a in range(len(nums)-2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            b = a + 1
            c = len(nums)-1
            while b < c:
                if b == c:
                    break
                elif (nums[b] + nums[c]) > (nums[a] * -1):
                    c -= 1
                elif (nums[b] + nums[c]) < (nums[a] * -1):
                    b += 1
                elif (nums[b] + nums[c]) == (nums[a] * -1):
                    combinations.append([nums[a], nums[b], nums[c]]) 
                    b += 1
                    c -= 1     
        combo = set()
        for j in combinations:
            combo.add(tuple(j))
        return combo

        
