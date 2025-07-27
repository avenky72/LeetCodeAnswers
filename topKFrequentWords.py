from collections import OrderedDict, deque
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = OrderedDict()
        for i in words:
            if i in frequency.keys():
                frequency[i] += 1
            else:
                frequency[i] = 1

        freq = OrderedDict(sorted(frequency.items(), key = lambda l: l[1], reverse = True))
        print(freq)

        output = []
        c = 0
        for word, count in freq.items():
            if c < k:
                output.append(word)
                c += 1
        
        return output
        
