import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        q = collections.deque()
        cnt = 0
        for c in s:
            if c not in h:
                h[c] = 1
                q.append(c)
            else:
                cnt = max(len(h), cnt)
                while q and c in h:
                    tmp = q.popleft()
                    del h[tmp]
                q.append(tmp)
                h[tmp] = 1
                h[c] = 1
        return max(len(h), cnt)
