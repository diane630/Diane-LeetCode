class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_valid(iterable) -> bool:
            valid = True
            number = {'1':0, '2':0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
            for item in iterable:
                if item == '.':
                    continue
                if item not in number:
                    valid = False
                    return valid
                number[item] += 1
                if number[item] > 1:
                    valid = False
                    return valid
            return valid
        
        #check 9 rows
        for row in range(9):
            cur_iterable = []
            for col in range(9):
                cur_iterable.append(board[row][col])
            if check_valid(cur_iterable) == False:
                return False
        #check 9 cols
        for col in range(9):
            cur_iterable = []
            for row in range(9):
                cur_iterable.append(board[row][col])
            if check_valid(cur_iterable) == False:
                return False
        
        #check 9 3x3 squares
        for left_top_cornor in [(0,0), (3,0), (6,0), (0,3), (3,3), (6,3), (0,6), (3,6), (6,6)]:
            cur_iterable = []
            for relavent_coordinate in [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]:
                row = left_top_cornor[0] + relavent_coordinate[0]
                col = left_top_cornor[1] + relavent_coordinate[1]
                cur_iterable.append(board[row][col])
            if check_valid(cur_iterable) == False:
                return False
        
        return True