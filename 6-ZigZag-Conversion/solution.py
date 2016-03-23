class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        s = list(s)
        g = numRows * 2 - 2
        res = [""] * numRows
        for i in xrange(len(s)):
            newIdx = i % g
            if newIdx >= g // 2:
                newIdx = g - newIdx
            res[newIdx] += s[i]
        return "".join(res)
            