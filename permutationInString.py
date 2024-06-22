class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        end = len(s1)
        start = 0
        letters = "qwertyuiopasdfghjklzxcvbnm"

        if len(s1) > len(s2):
            return False
        
        s1_d = {}
        for i in s1:
            if i in s1_d.keys():
                s1_d[i] += 1
            else:
                s1_d[i] = 1
        print("s1: ", s1_d)
                
        s2_d = {}
        s2s = s2[start:end]
        for i in s2s:
            if i in s2_d.keys():
                s2_d[i] += 1
            else:
                s2_d[i] = 1

        while len(s2) >= end:
            print("s2: ", s2_d)
            
            if s1_d == s2_d:
                return True
            else:
                
                """
                while len(s2) > end:
                    s2_d = {}
                    s2s = s2[start:end]
                    for i in s2s:
                        if i in s2_d.keys():
                            s2_d[i] += 1
                        else:
                            s2_d[i] = 1

                    if s1_d == s2_d:
                        return True
                    else:
                        start += 1
                        end += 1"""


                if end < len(s2):

                    if s2[end] in s2_d:
                        s2_d[s2[end]] += 1
                    else:
                        s2_d[s2[end]] = 1


                    if s2_d[s2[start]] == 1:
                        del s2_d[s2[start]]
                    else:
                        s2_d[s2[start]] -= 1
 
                start += 1
                end += 1

        return False        
