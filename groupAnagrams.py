# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sort = []
        sort_dict = {}
        for s in strs:
            sor = "".join(sorted(s))
            sort.append(sor)
        sorted_set = set(sort)
        sorted_list = list(sorted_set)
        #print(sorted_list)
        for i in sorted_list:
            temp_list = []
            for x in strs:
                j = ''.join(sorted(x))
                y = ''.join(sorted(i))
                #print(j,y)
                if j == y:
                    #print(j,y)
                    temp_list.append(x)
                #print(temp_list)
            sort_dict[i] = temp_list
        output = []
        #print(sort_dict)
        for k in sort_dict.values():
            output.append(k)
        return output

