class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend = abs(dividend) 
        divisor = abs(divisor)
        q = 0
        while dividend >= divisor:
            k = 0
            tmp = divisor
            while dividend >= tmp:
                q += 1 << k
                dividend -= tmp
                tmp <<= 1
                k += 1
        return q * sign
                