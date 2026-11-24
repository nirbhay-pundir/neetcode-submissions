class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                bit = 1 << (int(val) - 1)
                box_idx = (r // 3) * 3 + (c // 3)

                if (rows[r] & bit) or (cols[c] & bit) or (boxes[box_idx] & bit):
                    return False

                rows[r] |= bit
                cols[c] |= bit
                boxes[box_idx] |= bit

        return True