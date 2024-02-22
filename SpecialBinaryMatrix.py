#1582 Special Positions in a Binary Matrix
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        counter = True
        count = 0
        n = len(mat)
        m = len(mat[0])
        for i in range(0,n):
            for j in range(0,m):
                if mat[i][j] == 1:
                    counter = True
                    for k in range(0,m):
                        if k != j:
                            if mat[i][k] == 1:
                                print("fail")
                                counter = False
                    for l in range(0,n):
                        if l != i:
                            if mat[l][j] == 1:
                                print("fail")
                                counter = False
                if counter == True and mat[i][j] == 1:
                    count+=1
                    print(count)
        return count
