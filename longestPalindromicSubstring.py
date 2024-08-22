class Solution:
    def longestPalindrome(self, s: str) -> str:
        pally_len = 0
        pal = ""

        for i in range(len(s)):
            # Odd Length
            left, right = i, i
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                #s[left] == s[right]:
                    output = s[left:right+1]
                    if len(output) > len(pal):
                        pal = output
                        pally_len = len(pal)
                    left -= 1
                    right += 1

            # Even Length
            l, r = i, i+1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                #if s[l] == s[r]:
                    output = s[l:r+1]
                    if len(output) > len(pal):
                        pal = output
                        pally_len = len(pal)
                    l -= 1
                    r += 1
        return pal
