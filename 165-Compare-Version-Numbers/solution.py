class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if not version1 and not version2:
            return 0
        elif not version1:
            return -1
        elif not version2:
            return 1
        l1 = version1.split(".")
        l2 = version2.split(".")]
        k = 0
        for i in xrange(min(len(l1), len(l2)), -1, -1):
            if int(l1[i]) > int(l2[i]):
                return 1
            elif int(l1[i]) < int(l2[i]):
                return -1
            k += 1
        if len(l1) > k:
            return 1
        elif len(l2) > k:
            return -1
        return 0
        