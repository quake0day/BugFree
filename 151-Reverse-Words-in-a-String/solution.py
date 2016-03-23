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
        while r < len(s):
            if r != " ":
                r += 1
            elif r == " ":
                q.append(s[l:r-1])
                r += 1
                l = r
        q.append(s[l:r])
        while q:
            res.append(q.pop())
        return "".join(res)
                