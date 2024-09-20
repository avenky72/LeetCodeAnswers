class Solution:
    def shortestPalindrome(self, s: str):
        if len(s) == 1:
            return s

        prefix = self.pally(s)
        right = s[len(prefix):]
        left = right[::-1]
        output = left + s
        print(output)
        return output

    def pally(self, p: str):
        pally = ""
        for i in range(len(p)):
            if p[:i+1] == p[:i+1][::-1]:
                pally = p[:i+1]
        return pally

      # Takes the longest overall palindromic substring instead of from the initial index
        """
        prefix = self.longest_pally(s)
        print(prefix)
        left = s[0:prefix[1]]
        right = s[prefix[2]+1:len(s)]
        print(left, right)
        output = right[::-1] + left + prefix[0] + left[::-1] + right
        print(output)
        return output

    # Returns the longest palindromic substring from the initial index
    def longest_pally(self, p: str) -> str:
            pal = ""
            pal2 = ""
            left_index, right_index = 0, 0
            l_index, r_index = 0, 0

            # Odd Length
            for i in range(len(p)):
                left, right = i, i
                while left >= 0 and right <= len(p)-1 and p[left] == p[right]:
                    pally = p[left:right+1]
                    if len(pally) > len(pal):
                        pal = pally
                        left_index = left
                        right_index = right
                    left -= 1
                    right += 1


            # Even Length
                l, r = i, i+1
                while l >= 0 and r <= len(p)-1 and p[l] == p[r]:
                    pally = p[l:r+1]
                    if len(pally) > len(pal2):
                        pal2 = pally
                        l_index = l
                        r_index = r
                    l -= 1
                    r += 1
            if len(pal) > len(pal2):
                return [pal, left_index, right_index]
            else:
                return [pal2, l_index, r_index]
            """
        



                
        
