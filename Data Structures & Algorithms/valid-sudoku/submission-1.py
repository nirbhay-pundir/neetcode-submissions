class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set, col_set, grid_set = set(), set(), set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])

                m = ((i // 3) * 3) + (j // 3)
                n = (j % 3) + ((i % 3) * 3)
                if board[m][n] != ".":
                    if board[m][n] in grid_set:
                        return False
                    grid_set.add(board[m][n])
        return True
                