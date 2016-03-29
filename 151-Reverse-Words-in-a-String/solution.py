class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        s = list(s)
        self.reverse(s, 0, len(s)-1)
        
        idx = 0
        for i in xrange(len(s)):
            if s[i] == " ":
                self.reverse(s, idx, i-1)
                idx = i + 1
        self.reverse(s, idx, len(s) - 1)
        
        return "".join(s)
    
    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1