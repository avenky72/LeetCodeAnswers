class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        one = target[0]
        two = target[1]
        three = target[2]
        f_one = float('-inf')
        f_two = float('-inf')
        f_three = float('-inf')

        for i in triplets:
            if (max(f_one, i[0]) <= one) and (max(f_two, i[1]) <= two):
                if (max(f_three, i[2]) <= three):
                    f_one = max(f_one, i[0])
                    f_two = max(f_two, i[1])
                    f_three = max(f_three, i[2])
        
        if (f_one == one) and (f_two == two):
            if (f_three == three):
                return True
            else:
                return False
        else:
            return False

