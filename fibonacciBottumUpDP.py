class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [0, 1]
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            for i in range(2, n+1):
                temp = table[i-1] + table[i-2]
                table.append(temp)
            return table[-1]
