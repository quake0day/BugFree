class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.reverse(s, 0, len(s) - 1)
        n = len(s)
        beg = 0
        for r in xrange(len(s)):
            if s[r] ==  ' ':
                self.reverse(beg, r-1, s)
                beg = r + 1
            elif r == len(s) - 1:
                self.reverse(beg, r, s)
            
    
    def reverse(self, l, r, s):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
