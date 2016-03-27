class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            k = 0; tmp = divisor
            while dividend >= tmp:
                quotient += 1 << k
                dividend -= tmp
                tmp <<= 1
                k += 1
        return quotient * sign
                