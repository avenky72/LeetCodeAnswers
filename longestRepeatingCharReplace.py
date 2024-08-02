class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, right = 0, 0
        output = 0
        counter = {}

        while right < len(s):
            if s[right] in counter:
                counter[s[right]] += 1
            else:
                counter[s[right]] = 1  

            max_freq = max(counter.values())
            window = (right - left) + 1

            if window - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            
            window = (right - left) + 1
            output = max(output, window)
            right += 1

        return output



        """
        while right < len(s):
            counter = {}
            window = s[left:right]
            for letter in window:
                if letter in letter_count:
                    counter[letter] += 1
                else:
                    counter[letter] = 1
            freq_l = None
            freq_count = 0
            for letter, count in counter.items():
                if count > freq_count:
                    freq_l = letter
                    freq_count = count
            while (len(window) - freq_count) <= k:
                right += 1
                output = max(output, len(window))
            if (len(window) - freq_count) > k:
                left += 1

        return output
        """

