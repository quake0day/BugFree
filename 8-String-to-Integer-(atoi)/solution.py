class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return None
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s = str.lstrip()
        sign = 0
        if s[0] in ('+','-'):
            sign = 1 if s[0] == '-' else 0
            s = s[1:]
        res = 0
        digits = map(str, [i for i in xrange(10)])
        i = 0
        while i < len(s) and s[i] in digits:
            res = res * 10 + int(s[i])
            i += 1
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res * sign
        