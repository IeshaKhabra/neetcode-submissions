class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create 9 sets for 9 rows
        # rows[0] stores numbers found in row 0
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                # r//3 gives the box row 
                # c//3 gives the box col
                box_index = (r//3) * 3 + (c//3)
                # if the value has already appeared in the same row then invalid
                if value in rows[r]:
                    return False
                
                if value in columns[c]:
                    return False
                
                if value in boxes[box_index]:
                    return False
                
                rows[r].add(value)
                columns[c].add(value)
                boxes[box_index].add(value)
        return True