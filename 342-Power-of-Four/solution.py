class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        return ((num - 1) & num) == 0 and (num & 0x55555555) != 0
        