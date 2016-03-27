class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        if not(0 <= i < len(grid)) or not ( 0 <= j < len(grid[0])) or grid[i][j] != '1':
            return 
        grid[i][j] = '#'
        directions = zip([1,0,-1,0],[0,1,0,-1])
        for d in directions:
            self.dfs(grid, i+d[0],j+d[1])
        