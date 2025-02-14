class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq.keys():
                freq[i] += 1
            else:
                freq[i] = 1
        
        elements = []
        for i in range(k):
            key = max(freq, key = freq.get)
            elements.append(key)
            del freq[key]
        
        return elements
