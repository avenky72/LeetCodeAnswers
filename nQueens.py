class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        row = set()
        # postive diagonal is row + col
        pdiag = set()
        # negative diagonal is row - col
        ndiag = set()
        board = [["."] * n for i in range(n)]
        
        def queenBT(col):
            if col >= n:
                solution = ["".join(col) for col in board]
                result.append(solution)
                return  

            # For each row, check if the row is available or in the row set
            # Then check both its pos and neg diagonals to see if they're in the set
            # If all is available, then you can place it in that cell
            for r in range(n):
                if r in row or (r+col) in pdiag or (r-col) in ndiag:
                    pass
                else:
                    row.add(r)
                    pdiag.add(r+col)
                    ndiag.add(r-col)
                    board[r][col] = "Q"

                    # Do the backtracking
                    queenBT(col+1)

                    # Undo everything
                    row.remove(r)
                    pdiag.remove(r+col)
                    ndiag.remove(r-col)
                    board[r][col] = "."
            
        queenBT(0)
        return result


                
