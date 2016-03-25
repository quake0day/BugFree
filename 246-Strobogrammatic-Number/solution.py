class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        h = {"6":"9", "8":"8","9":"6","1":"1","0":"0"}
        l, r = 0, len(num)-1
        while l <= r:
            if num[l] not in h or num[r] not in h or num[l] != h[num[r]]:
                return False
            l += 1
            r -= 1
        return True
        