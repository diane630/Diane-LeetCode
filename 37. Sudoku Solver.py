class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(r: int, c:int) -> bool:
            # check row
            nonrepeat = set()
            for i in range(9):
                if board[r][i] in nonrepeat:
                    return False
                if board[r][i].isnumeric():
                    nonrepeat.add(board[r][i])
            # check col
            nonrepeat = set()
            for i in range(9):
                if board[i][c] in nonrepeat:
                    return False
                if board[i][c].isnumeric():
                    nonrepeat.add(board[i][c]) 
            # check 3x3 block
            nonrepeat = set()
            for i in range(r//3*3, r//3*3 + 3):
                for j in range(c//3*3, c//3*3 + 3):
                    if board[i][j] in nonrepeat:
                        return False
                    if board[i][j].isnumeric():
                        nonrepeat.add(board[i][j])
            return True
        
        def dfs_helper(board: List[List[str]]):
            # find next unfilled pos
            # if early_return:
            #     return True
            # early_return = False
            c = 0
            ret = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        c += 1
                        for num in range(1, 10):
                            board[i][j] = str(num)
                            if is_valid(i, j):
                                ret = dfs_helper(board)
                            if ret: return True
                            board[i][j] = "."
            if c == 0:
                return True
        
        dfs_helper(board)
        return board
            
                