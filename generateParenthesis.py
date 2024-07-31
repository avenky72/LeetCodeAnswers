class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        output = []

        def parenBT(op, close):
            if op == close == n:
                output.append("".join(res))
                return
            
            # Add open parenthesis when its count is less than n
            if op < n:
                res.append("(")
                parenBT(op+1, close)
                res.pop()

            # Add closed parenthesis when its count is less than open's
            if close < op:
                res.append(")")
                parenBT(op, close+1)
                res.pop()
        
        parenBT(0,0)
        return output
