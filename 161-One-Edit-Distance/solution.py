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
        L = True
        if m == n:
            l1, l2 = 0, 0
            
            while l1 < m and l2 < n:
                if s[l1] != t[l2] and L == True:
                    L = False
                elif s[l1] != t[l2] and L == False:
                    return False
                l1 += 1
                l2 += 1
        elif abs(m-n) == 1:
            l1, l2 = 0, 0
            while l1 < m and l2 < n:
                if s[l1] != s[l2] and L == True:
                    if l1 + 1 < m and s[l1+1] == t[l2]:
                        l1 += 1
                        L = False
                    elif l2 + 1 < n and s[l1] == t[l2 + 1]:
                        l2 += 1
                        L = False
                    else:
                        return False
                elif s[l1] != s[l2] and L == False:
                    return False
                l1 += 1
                l2 += 1
        return L == False