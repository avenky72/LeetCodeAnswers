class Solution(object):
    def exist(self, board, word):
        
        term = len(word)

        # Case where there is only a single character in the board and it's the target
        if word == board[0][0]:
            return True

        def wordBT(row, col, letter):

            # Base Case: If the length of the word is the same as the target
            if letter == term:
                return True

            # Base Case: If the cell doesn't contain the next letter
            if board[row][col] != word[letter]:
                return False

            # The cell contains the next letter, so mark it as seen
            temp = board[row][col]
            board[row][col] = "#"

            # Need to check all adjacent cells to see if the next letter is there
            # Check to see the adjacent exists
            """if (row - 1) >= 0 and (row + 1) <= len(board):
                if (col - 1) >= 0 and (col + 1) <= len(board[0]):
                    for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:"""
            for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:
                next_row = row + x
                next_col = col + y
                if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                    if wordBT(next_row, next_col, letter + 1):
                        return True

            # The adjacent doesn't exist or the next letter isn't in the adjacent cell
            board[row][col] = temp
            return False

        # Find starting cell/letter
        for r in range(len(board)):
            for c in range(len(board[0])):
                if wordBT(r, c, 0):
                    return True
        return False


    """
        words = []
        for i in word:
            words.append(i)

        row, col = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    row = r
                    col = c
                    break
        
        def wordBT(row, col):
            visited[len(board)][len(board[0])]
            term = ''
            if len(term) == len(word):
                term_set = set(term)
                word_set = set(word)
                if term_set == word_set:
                    return True
            
            curr = board[row][col]
            
            if curr in words:
                term += curr
                words.remove(curr)
                if row < len(board):
                    if board[row+1, col] in words:
                        wordBT(row + 1, col)
                if col < len(board[0]):
                    if board[row, col + 1] in words:
                        wordBT(row, col + 1)
            else: 
                for r in range(len(board), row):
                    for c in range(len(board[0]), col):
                        if board[r][c] == word[0]:
                            row = r
                            col = c
                            break
    """

                        
