#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {"]":"[", "}":"{", ")":"("}
        p = []

        # check edges
        if s[0] in pairs:
            return False
        elif s[-1] not in pairs:
            return False
        else:
            for i in s:
                if i in pairs.values():
                    p.append(i)
                elif i in pairs.keys():
                    # need to check to make sure list/stack isn't empty or else index out of bounds error
                    if len(p) > 0:
                        if pairs[i] != p[-1]:
                            return False
                        elif pairs[i] == p[-1]:
                            p.pop()
                    else:
                        return False
        if len(p) == 0:
            return True
        else:
            return False
