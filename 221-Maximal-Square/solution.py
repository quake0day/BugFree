class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        dp = [[0] * len(matrix[0]) for _ in xrange(len(matrix))]
        max_ = 0
        for i in xrange(len(matrix[0])):
            dp[0][i] = int(matrix[0][i])
            max_ = max(dp[0][i], max_)
        for j in xrange(len(matrix)):
            dp[j][0] = int(matrix[j][0])
            max_ = max(dp[j][0], max_)
            
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    max_ = max(dp[i][j], max_)
        return max_ ** 2
        
        