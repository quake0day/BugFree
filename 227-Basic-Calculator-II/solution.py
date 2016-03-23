class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def nextint(s,i):
            res = 0
            while i < len(s) and s[i] not in '+-*/':
                res = res * 10 + ord(s[i]) - ord('0')
                i += 1
            return (res, i)
        
        s = s.replace(' ', '')
        stack = []
        i = 0
        tmp, i = nextint(s,0)
        stack.append(tmp)
        while i < len(s):
            op = s[i]
            tmp, i = nextint(s, i+1)
            if op == '+': stack.append(tmp)
            elif op == '-': stack.append(-tmp)
            elif op == '*': stack[-1] *= tmp
            elif op == '/': stack[-1] = stack[-1] // tmp if stack[-1] >= 0 else -((-stack[-1])//tmp)
        res = 0
        for num in stack:
            res += num
        return res