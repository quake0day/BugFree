class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        max_int = 2147483647
        min_int = -2147483648
        if dividend == min_int and divisor == -1:
            return max_int
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0; count = 0; res = 0
        a = abs(dividend); b = abs(divisor)
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
            
                
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        return res