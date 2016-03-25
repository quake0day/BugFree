class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.m, self.n = len(matrix), len(matrix[0]) if matrix else 0
        self.matrix = [[0]*(self.n) for _ in range(self.m)]
        self.sums = [[0] * (self.n+1) for _ in xrange(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
        
        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff, self.matrix[row][col], i = val-self.matrix[row][col], val, row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.sums[i][j] += diff
                j += (j & -j)
            i += (i & -i)
        
    def sum(self, row, col):
        r, i = 0, row + 1
        while i:
            j = col + 1
            while j:
                r += self.sums[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return r
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum(row2, col2) + self.sum(row1-1, col1-1) - self.sum(row1-1, col2) - self.sum(row2, col1-1)
        
        

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)