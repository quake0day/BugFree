class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {"{":"}", "(":")","[":"]"}
        stack = []
        for p in s:
            if p in ("{","(","["):
                stack.append(p)
            elif stack and m[stack[-1]] == p:
                stack.pop()
            else:
                return False
        return len(stack) == 0
        