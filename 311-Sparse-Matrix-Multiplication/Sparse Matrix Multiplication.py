class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(B)
        B = zip(*B)
        res = []
        for row in A:
            if not any(row):
                res.append([0] * n)
            else:
                tmp = []
                i = 0
                for col in B:
                    tmp.append(sum(map(lambda (x,y): x*y, zip(row,col))))
                    i += 1
                    print tmp
                res.append(tmp)
        return res
