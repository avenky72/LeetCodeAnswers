class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = []
        tt = []
        for i in s:
            if i != "#":
                ss.append(i)
            else:
                if len(ss) > 0:
                    ss.pop()
        
        for j in t:
            if j != "#":
                tt.append(j)
            else:
                if len(tt) > 0:
                    tt.pop()

        if ss == tt:
            return True
        else:
            return False

        
