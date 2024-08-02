class Solution:
    def countSubstrings(self, s: str) -> int:
        pallys = 0
        #pal = ""

        for i in range(len(s)):
            # Odd Length
            left, right = i, i
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                #s[left] == s[right]:
                    pallys += 1
                    left -= 1
                    right += 1

            # Even Length
            l, r = i, i+1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                #if s[l] == s[r]:
                    pallys += 1
                    l -= 1
                    r += 1
        return pallys
            

