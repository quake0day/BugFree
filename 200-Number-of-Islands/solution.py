class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        
        q = []
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    res += 1
                    q.append((i,j))
                    while q:
                        x, y = q.pop()
                        grid[x][y] = '#'
                        for d in directions:
                            nx, ny = x + d[0], y + d[1]
                            if 0 <= nx < m and 0 <= ny < n:
                                if grid[nx][ny] == '1':
                                    q.append((nx,ny))
        return res
        