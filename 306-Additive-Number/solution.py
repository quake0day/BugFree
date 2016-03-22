class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        self.Flag = False

        if len(num) <= 2:
            return self.Flag

        def helper(num, tmp, final_res):
            if len(num) == 0:
                self.Flag = True
                return
            if len(tmp) > 1:
                for i in xrange(1, len(num)+1):
                    if (tmp[-1] + tmp[-2]) ==  int(num[:i]):
                        helper(num[i:], tmp+[int(num[:i])], final_res)
                    else:
                        return 
            else:
                for i in xrange(1, len(num)+1):
                    helper(num[i:], tmp+[int(num[:i])], final_res)


        final_res = []
        for i in xrange(len(num)):
            helper(num, [], final_res)
        return self.Flag