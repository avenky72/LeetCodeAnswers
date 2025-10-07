class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        import numpy as np

        cache = np.empty((m, n))
        cache[m-1][n-1] = 1

        for i in range(n-1):
            cache[m-1][i] = 1
        for i in range(m-1):
            cache[i][n-1] = 1


        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                cache[i][j] = cache[i+1][j] + cache[i][j+1]

        return int(cache[0][0])

            
        
