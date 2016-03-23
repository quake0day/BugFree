class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack2:
            self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack1 and not self.stack2:
            return True
        return False
        