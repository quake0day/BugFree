class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """

        self.vec2d = vec2d
        self.vec = []
        self.flatten(vec2d)
        self.x = 0
    
    def flatten(self, vec):
        for v in vec:
            if isinstance(v, list):
                self.flatten(v)
            else:
                self.vec.append(v)
        

    def next(self):
        """
        :rtype: int
        """
        tmp = None
        if self.x < len(self.vec):
            tmp = self.vec[self.x]
            self.x += 1
        return tmp
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.x < len(self.vec)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())