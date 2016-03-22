class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in xrange(1, n // 2 + 1):
            for j in xrange(1, (n-i) // 2 + 1):
                first, second, rest = num[:i], num[i:i+j], num[i+j:]
                if ((len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0')):
                    continue
                while rest:
                    sum_str = str(int(first) + int(second))
                    if sum_str == rest:
                        return True
                    elif rest.startswith(sum_str):
                        first, second, rest = (second, sum_str, rest[len(sum_str):])
                    else:
                        break
        return False