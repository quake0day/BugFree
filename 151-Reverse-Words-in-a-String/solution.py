class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.lstrip()
        q = collections.deque()
        l,r = 0, 0
        res = []
        while l < len(s):
            if r != " ":
                r += 1
            elif r == " ":
                q.append(s[l:r])
                r += 1
                l = r
        while q:
            res.append(q.pop())
        return res
                