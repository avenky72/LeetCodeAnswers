class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        output = []
        combo = []

        def sumsBT():
            if sum(combo) == target:
                sorted_combo = sorted(combo)
                if sorted_combo not in output:
                    output.append(sorted_combo)
                return
            
            for i in candidates:
                if (i+sum(combo)) <= target:
                    combo.append(i)
                    sumsBT()
                    combo.remove(i)

        """def remove_dups(l):
            unique = set(tuple(sorted(l)) for i in l)
            return [list(i) for i in unique]
            """
            
        sumsBT()
        print(output)
        return output
        #return remove_dups(output)
