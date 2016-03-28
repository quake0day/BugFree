class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:
            return ""
        h = collections.Counter(t)
        cnt = 0
        L = len(s) + 1
        start = L
        l, r = 0, 0
        
        while r < len(s):
            if s[r] in h:
                h[s[r]] -= 1
                cnt += 1 if h[s[r]] >= 0 else 0
            while cnt == len(t):
                if r - l + 1 < L:
                    L = r - l + 1
                    start = l
                if s[l] in h:
                    h[s[l]] += 1
                    cnt -= 1 if h[s[l]] > 0 else 0
                l += 1
            r += 1
        return s[start:start+L]