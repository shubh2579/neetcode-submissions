class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                
                # 1. Check Rows
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # 2. Check Columns
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # 3. Check 3x3 Boxes
                box_idx = (r // 3) * 3 + (c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)
                
        return True
            