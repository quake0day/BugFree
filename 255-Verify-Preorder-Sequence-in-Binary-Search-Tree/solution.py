class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        lower = -float('inf')
        stack = []
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True

        