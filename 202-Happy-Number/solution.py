class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        h = {}
        while n != 1 and n not in h:
            h[n] = True
            num = str(n)
            res = 0
            for s in num:
                res += int(s) ** 2
            n = res
        return n == 1
                