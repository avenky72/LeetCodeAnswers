#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pal = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                pal += i
        pal = pal.lower()
        print(pal)
        j = 0
        k = len(pal)-1
        while j < k:
            if pal[j] != pal[k]:
                return False
            j += 1
            k -= 1
        return True


        
        

        
