class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        res = [[1]]
        numRows -= 1
        while numRows > 0:
            res.append([1] + [a+b for a,b in zip(res[-1][:-1], res[-1][1:])] +[1])
            numRows -= 1
        return res
        