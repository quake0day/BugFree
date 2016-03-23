class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.split()[::-1]
                