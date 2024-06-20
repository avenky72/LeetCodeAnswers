class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        temp = [0] * len(temperatures)


        for i in range(len(temperatures)-1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    temp[i] = j - i 
                    break


        return temp
