class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        n = len(s)
        l, r = 0, 0
        while r < n:
            if s[r] != ' ':
                r += 1
            elif s[r] == ' ':
                self.reverse(l, r-1, s)
                r += 1
                l = r

        return self.reverse(0, n-1, s)
            
    
    def reverse(self, l, r, s):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
