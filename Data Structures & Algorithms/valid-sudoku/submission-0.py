class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = [set() for _ in range(9)]
        col_hash = [set() for _ in range(9)] 
        boxes_hash = [set() for _ in range(9)]  

        for r_index, row in enumerate(board):
            for c_index, cell in enumerate(row):
                if cell == ".":
                    continue
                if cell in col_hash[c_index]:
                    return False
                col_hash[c_index].add(cell)

                if cell in row_hash[r_index]:
                    return False
                row_hash[r_index].add(cell)

                box_position = self.get_square_index(r_index,c_index)

                if cell in boxes_hash[box_position]:
                    return False
                boxes_hash[box_position].add(cell)

        return True

    def get_square_index(self,row: int, col: int) -> int:
        box_row = row // 3
        box_col = col // 3
        return box_row * 3 + box_col


        