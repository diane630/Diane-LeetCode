class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        m = len(matrix)
        n = len(matrix[0])
        
        # row sum from matrix[i][0] .... matrix[i][j]
        self.path_sum_row = [[0 for j in range(n)] for i in range(m)]
        # col sum from matrix[0][j] .... matrix[i][j]
        self.path_sum_col = [[0 for j in range(n)] for i in range(m)]
        # region sum from matrix[0][0] .... matrix[i][j]
        self.path_sum_region = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if j == 0: 
                    self.path_sum_row[i][j] = matrix[i][j]
                else:
                    self.path_sum_row[i][j] = self.path_sum_row[i][j-1] + matrix[i][j]
        for j in range(n):
            for i in range(m):
                if i == 0: 
                    self.path_sum_col[i][j] = matrix[0][j]
                else:
                    self.path_sum_col[i][j] = self.path_sum_col[i-1][j] + matrix[i][j]
        for i in range(m):
            for j in range(n):
                if i == 0: 
                    self.path_sum_region[i][j] = self.path_sum_row[i][j]
                elif j == 0:
                    self.path_sum_region[i][j] = self.path_sum_col[i][j]
                else:
                    self.path_sum_region[i][j] = self.path_sum_region[i][j-1] + self.path_sum_col[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1 == 0 and row1 == 0:
            return self.path_sum_region[row2][col2]
        elif col1 == 0:
            return self.path_sum_region[row2][col2] - self.path_sum_region[row1-1][col2]
        elif row1 == 0:
            return self.path_sum_region[row2][col2] - self.path_sum_region[row2][col1-1]
        else:
            return self.path_sum_region[row2][col2] + self.path_sum_region[row1-1][col1-1] - self.path_sum_region[row2][col1-1] - self.path_sum_region[row1-1][col2]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)