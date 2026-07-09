class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {}
        for row in range(9):
            row_seen = set()
            column_seen = set()
            
            for column in range(9):
                #checking boxes
                box_row = row // 3
                box_col = column // 3

                #getting and chekcing each row
                numr = board[row][column]
                if numr != '.':
                    if numr in row_seen:
                        return False
                    row_seen.add(numr)

                # getting and chekcing by each column
                numc = board[column][row]
                if numc != '.':
                    if numc in column_seen:
                        return False
                    column_seen.add(numc)

                #checking boxes
                if (box_row, box_col) not in boxes:
                    boxes[(box_row, box_col)] = set()
                if numr != '.':
                    if numr in boxes[(box_row, box_col)]:
                        return False
                    boxes[(box_row, box_col)].add(numr)
            
                
            

        return True