class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {0:0, 1:1}

        def fibo(x):
            if x in cache.keys():
                return cache[x]
            else:
                cache[x] = fibo(x-1) + fibo(x-2)
                return cache[x]

        return fibo(n)
        
