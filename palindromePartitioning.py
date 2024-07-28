class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        output = []
        pal = []

        n = len(s)

        def pallyBT(i = 0):
            if i == n:
                output.append(pal[:])
                return
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    pal.append(s[i:j+1])
                    pallyBT(j+1)
                    pal.pop()
        pallyBT(0)
        return output
            
            
        
        pallyBT()
        return output
        
