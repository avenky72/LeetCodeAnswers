class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        sub = []
        
        if len(s) == 1:
            return 1

        for i in s:
            print(sub)
            if i in sub:
                index = sub.index(i)
                sub = sub[index+1:]
                sub.append(i)
            elif i not in sub:
                sub.append(i)
            longest = max(longest, len(sub))
        return longest    

        
