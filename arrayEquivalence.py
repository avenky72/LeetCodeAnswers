# Check if two arrays containing various string elements contain the same elements
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word1_s = ''
        for i in word1:
            word1_s += i
        for i in word2:
            if i in word1_s:
                return True
            else:
                return False
       
