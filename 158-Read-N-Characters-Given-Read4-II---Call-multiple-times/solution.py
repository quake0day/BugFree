# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.q = collections.deque()
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n == 0:
            return 0
        idx = 0
        while n > 0 and self.q:
            buf[idx] = self.q.popleft()
            idx += 1
            n -= 1
        while n > 0:
            buf4 = [""] * 4 
            l = read4(buf4)
            if not l:
                return idx 
            if l > n:
                for c in buf4[n:l]:
                    self.q.append(c)
            for i in xrange(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx
                