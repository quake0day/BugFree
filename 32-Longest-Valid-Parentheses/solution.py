class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        L = 0
        M = 0
        curL = 0
        for p in s:
            if p == '(':
                stack.append(p)
            elif p == ')' and stack and stack[-1] == '(':
                stack.pop()
                curL += 2
            else:
                curL = 0
            if not stack:
                L = max(curL, L)
        stack = []
        curL = 0
        for q in s[::-1]:
            if q == ')':
                stack.append(q)
            elif q == '(' and stack and stack[-1] == ')':
                stack.pop()
                curL += 2
            else:
                curL = 0
            if not stack:
                M = max(curL, M)
        return max(L,M)