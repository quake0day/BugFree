class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in xrange(rowIndex):
            row = [u+v for u, v in zip(row+[0], [0]+row)]
        return row