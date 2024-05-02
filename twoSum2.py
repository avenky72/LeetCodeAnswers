# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        index = [0,0]
        for l in range (0, len(numbers)):
            print(i, j)
            if (numbers[i] + numbers[j]) > target:
                j-=1
            elif (numbers[i] + numbers[j]) < target:
                i+=1
            elif (numbers[i] + numbers[j]) == target:
                index[0] = i+1
                index[1] = j+1
            elif i == j:
                return -1
        return index
    
