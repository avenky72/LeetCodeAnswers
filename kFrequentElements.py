# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        output = []
        count_set = set(nums)
        for i in count_set:
            counter = 0
            for j in nums:
                if i == j:
                    counter += 1
            count[i] = counter
        
        for j in range(k):
            temp = max(count, key=count.get)
            output.append(temp)
            del count[temp]
        return output

        
