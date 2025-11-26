class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        count the number of binary substrings with equal amount of 0s and 1s, but the 1s and 0s both have to be consecutive
        """

        output = 0

        # loop through to find transitions

        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                l = i
                r = i + 1
                # branching out both sides until either one finds a different parity
                while (l >= 0 and r <= len(s)-1):
                    if (s[l] == s[i] and s[r] == s[i+1]):
                        output += 1
                        l -= 1
                        r += 1
                    else:
                        break
        return output
