class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grams = {}
        for string in strs:
            if tuple(sorted(string)) in grams.keys():
                grams[tuple(sorted(string))].append(string)
            else:
                grams[tuple(sorted(string))] = [string]

        anagrams = []
        for key, value in grams.items():
            anagrams.append(value)
        return anagrams
