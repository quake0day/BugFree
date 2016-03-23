class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)
        self.stack1.append(x)
        
        

    def pop(self):
        """
        :rtype: nothing
        """
        tmp = self.stack1.pop()
        if tmp == self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        