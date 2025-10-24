class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def recursive_check (i, j):
            
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + recursive_check(i+1, j+1)
            
            else:
                return max(recursive_check(i+1, j), recursive_check(i, j+1))

        return recursive_check(0, 0)
            
