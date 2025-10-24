class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}

        def recursive_check (i, j):
            
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            else:

                if text1[i] == text2[j]:
                    cache[(i, j)] = 1 + recursive_check(i+1, j+1)
                
                else:
                    cache[(i, j)] = max(recursive_check(i+1, j), recursive_check(i, j+1))

            return cache[(i, j)]


        return recursive_check(0, 0)
            
