class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for i in strs:
            s = sorted(i)
            si = "".join(s)


            # if not a seen anagram, create a new dictionary key-value pair
            if si not in seen:
                seen[si] = [i]

            # if a seen anagram, add that word to the existing list within the key-value pair
            else:
                seen[si].append(i)

        # at the end, loop through the dictionary and put all the keys (which are lists) into the output
        return list(seen.values())
