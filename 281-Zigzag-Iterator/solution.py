class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q1 = collections.deque(v1)
        self.q2 = collections.deque(v2)
        self.S = True
        

    def next(self):
        """
        :rtype: int
        """
        if not self.q1 and not self.q2:
            return []
        elif not self.q1:
            return self.q2.popleft()
        elif not self.q2:
            return self.q1.popleft()
            
        if self.S and self.q1:
            self.S = False
            return self.q1.popleft()
        elif self.S == False and self.q2:
            self.S = True
            return self.q2.popleft()
        
        
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q1) + len(self.q2) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())