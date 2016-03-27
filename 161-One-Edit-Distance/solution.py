class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if not s and not t:
            return False
        if abs(m - n) > 1:
            return False
        l, r = 0, 0
        edit_dis = 0
        while l < m and r < n:
            if s[l] != t[r]:
                edit_dis += 1
                if l + 1 < m and s[l+1] == t[r]:
                    l += 1
                elif r + 1 < n and s[l] == t[r+1]:
                    r += 1
            if edit_dis > 1:
                return False
            l += 1
            r += 1
        edit_dis += (m - l) + (n - r)
        return edit_dis == 1
