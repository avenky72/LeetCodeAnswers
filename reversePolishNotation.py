import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operands = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': lambda a, b: int(operator.truediv(a, b))}
        for i in tokens:
            if i in operands:
                a = stack.pop()
                b = stack.pop()
                c = operands[i](b, a)
                stack.append(c)
            else:
                stack.append(int(i))
        return stack[0]
