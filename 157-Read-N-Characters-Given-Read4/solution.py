# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n == 0:
            return 0
            
        buf4 = [""] * 4
        idx = 0
        num_read = read4(buf4)
        while num_read != 0 and idx < n:
            if num_read + idx >= n:
                for i in range(n - idx):
                    buf[idx+i] = buf4[i]
                return n
            else:
                for i in range(num_read):
                    buf[idx+i] = buf4[i]
                idx += num_read
                num_read = read4(buf4)
        return idx