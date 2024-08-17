class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_dict = {}
        for i in range(len(s)):
            if s[i] not in letter_dict:
                letter_dict[s[i]] = [i, i]
            else:
                letter_dict[s[i]][1] = i
                
        size = 0
        end = letter_dict[s[0]][1]
        output = []
        
        for i in range(len(s)):
            end = max(end, letter_dict[s[i]][1])
            size += 1
            if i == end:
                output.append(size)
                print(output)
                size = 0
        return output

            
