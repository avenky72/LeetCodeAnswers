class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""

        for i in range(len(strs[0])):
            index = strs[0][i]
            for j in strs:
                if i >= len(j) or j[i] != index:
                    return prefix
            prefix += index
        return prefix
            
        
