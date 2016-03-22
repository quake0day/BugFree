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
        l1 = version1.split(".")[::-1]
        l2 = version2.split(".")[::-1]
        for i in xrange(min(len(l1), len(l2))):
            if int(l1[i]) > int(l2[i]):
                return 1
            elif int(l1[i]) < int(l2[i]):
                return -1
        if len(l1) > i:
            return 1
        elif len(l2) > i:
            return -1
        return 0
        