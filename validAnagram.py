#242 Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = []
        t_list = []
        s2_list = []
        for i in s:
            s_list.append(i)
        for j in t:
            t_list.append(j)
        sort_s = sorted(s_list)
        sort_t = sorted(t_list)
        if sort_s == sort_t:
            return True
        else:
            return False
    """
    Without the Sorted Method:
        s_list = []
        t_list = []
        s2_list = []
        for i in s:
            s_list.append(i)
        for j in t:
            t_list.append(j)
            if j in s_list:
                pass
            else:
                return False
        for k in s:
            s2_list.append(k)
            if k in t_list:
                pass
            else:
                return False
        if len(s_list) != len(t_list):
            return False 
            
            return True
 """
        
