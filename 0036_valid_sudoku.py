# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        create funtion to check list of lengnth 9 for duplicate numbers
        
        check rows
        check culumns
        check boxes
            create new list for box | list slicing
        """
        
        ''' This code sucks '''
        
        # rows
        if IsInvalidRows(board):
            return False
        
        # culumns
        for culumn in range(9):
            if isInvalidSection([board[row][culumn] for row in range(9)]):
                return False
        
        # boxes
        for row_start in range(0, 9, 3):
            boxes = [[], [], []]
            for row in range(row_start, row_start+3):
                for column, box in zip(range(0, 9, 3), boxes):
                    box.extend(board[row][column:column+3])
            if IsInvalidRows(boxes):
                return False
            
        return True
    
def IsInvalidRows(arrays) -> bool:
    return any(map(isInvalidSection, arrays))

def isInvalidSection(array: list) -> bool:
    seen = set()
    for item in array:
        if item == ".":
            continue
        if item in seen:
            return True
        seen.add(item)
    return False
