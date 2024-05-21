class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        w = ''
        for i in words:
            w += i[0]
        if w == s:
            return True
        else:
            return False
