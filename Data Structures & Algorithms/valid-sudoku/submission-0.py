class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = [set() for _ in range(9)]
        col_map = [set() for _ in range(9)]
        grid_map = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_map[i]:
                        return False
                    row_map[i].add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col_map[i]:
                        return False
                    col_map[i].add(board[j][i])

                m = ((i // 3) * 3) + (j // 3)
                n = (j % 3) + ((i % 3) * 3)
                if board[m][n] != ".":
                    if board[m][n] in grid_map[i]:
                        return False
                    grid_map[i].add(board[m][n])
        return True
                