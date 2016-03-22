class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def helper(num, tmp, final_res, s3):
            if len(num) == 0:
                return True
            if len(tmp) > 1:
                if tmp[-2]+tmp[-1] == s3:
                    tmp.append(s3)
                else:
                    return False
            for i in xrange(1, len(num)):
                helper(num[i:], tmp+[int(num[:i])], final_res, int(num[:i]))
           
        final_res = []
        for i in xrange(len(num)):
            if helper(num, [], final_res, 0):
                return True
        return False