class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
            
        if p[-1] == '*':
            if s and (p[-2] in [s[-1], '.']):
                return self.isMatch(s, p[:-2]) or self.isMatch(s[:-1], p)
            else:
                return self.isMatch(s, p[:-2])
        else:
            if s and (p[-1] in [s[-1],'.']):
                return self.isMatch(s[:-1], p[:-1])
            else:
                return False

                    
                        
             
                
        