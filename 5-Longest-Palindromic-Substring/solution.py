class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxL = 1
        for i in xrange(len(s)):
            # aba
            l, r = i,i
            L = 0
            while l >= 0 and r <len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    L += 1
                    maxL = max(maxL, L)
                else:
                    break
            # abba
            if i - 1 >= 0 and s[i-1] == s[i]:
                l, r = i-1, i
                L = 0
                while l >= 0 and r <len(s):
                    if s[l] == s[r]:
                        l -= 1
                        r += 1
                        L += 1
                        maxL = max(maxL, L)
                    else:
                        break
        return maxL
                    
                
                
                
        