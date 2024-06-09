class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        length = 0
        subset = set()
        
        while end < len(s):
            if s[end] in subset:
                subset.remove(s[start])
                start +=1
            else:
                subset.add(s[end])
                length = max(length, len(subset))
                end += 1
        return length
            


