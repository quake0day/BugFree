class Solution(object):
    
    def gen(self, s):
        alpha = [chr(i) for i in xrange(256)]
        h = {}
        n =[]
        for i in xrange(len(s)):
            if s[i] in h:
                n.append(h[s[i]])
            else:
                h[s[i]] = alpha[len(h)]
                n.append(h[s[i]])
        return n
        
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t) == 0 or len(s) == len(t) == 1:
            return True
        return self.gen(s) == self.gen(t)