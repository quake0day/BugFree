class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = s.split()
        k = len(s)-1
        while not s[k] and k >= 0:
            k -= 1
        return len(s[k]) if k >= 0 else 0
        