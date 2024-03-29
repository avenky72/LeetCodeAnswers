# Determine if String Halves Are Alike
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i = len(s)/2
        a = s[0:i]
        b = s[i:]
        vowels = ['a', 'e', 'i', 'o', 'u']
        counter_a = 0
        counter_b = 0
        for i in a:
            if i in vowels:
                counter_a += 1
        for j in b:
            if j in vowels:
                counter_b += 1
        if counter_a == counter_b:
            return True
        else:
            return False
