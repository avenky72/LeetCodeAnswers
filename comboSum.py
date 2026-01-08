class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # add number → dfs(same index) → remove number (backtrack)

        output = []
        combo = []
        candidates.sort()

        def dfs(start, remaining):

            if remaining == 0:
                output.append(combo.copy())
                return

            elif remaining < 0:
                return

            
            for i in range(start, len(candidates)):
                curr = candidates[i]

                if curr > remaining:
                    break
                else:
                    combo.append(curr)
                    dfs(i, remaining-curr)
                    combo.pop()

        dfs(0, target)
        return output

                    

            
