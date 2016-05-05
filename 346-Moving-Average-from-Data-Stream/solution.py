class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.avg = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.avg = (self.size * self.avg + val) / (self.size + 1)
        self.size += 1
        return self.avg
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)