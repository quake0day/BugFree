import collections

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = collections.Counter(s)
        values = map(lambda x: x%2, h.values())
        return values.count(1) in [1,0]
        