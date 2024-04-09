# Return the Hamming weight of a positive integer
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        def convert(num):
            bin = []  
            while num >= 1:
                temp = num % 2  
                bin.insert(0, temp)  
                num = num / 2  
            return bin
        count = 0
        for i in convert(n):
            if i == 1:
                count+=1
        return count
        
