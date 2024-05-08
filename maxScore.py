#Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        score = 0
        r_str = ''
        l_str = ''
        zero_count = 0
        one_count = 0

        for i in range(1,len(s)):
            s1 = s[0:i] 
            s2 = s[i:len(s)]
            print(s1, s2)
            for j in s1:
                if j == '0':
                    zero_count += 1
            for k in s2:
                if k == '1':
                    one_count += 1
            print(one_count, zero_count)
            if (one_count + zero_count) > score:
                score = one_count + zero_count
            one_count = 0
            zero_count = 0
        return score
        
