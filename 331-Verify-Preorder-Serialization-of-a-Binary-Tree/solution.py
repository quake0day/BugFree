class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        print preorder
        if len(preorder) == 1 and preorder[0] == '#':
            return True
        stack = []
        preorder = preorder.split(",")
        for s in preorder:
            if s != '#':
                stack.append(s)
            elif s == '#':
                if len(stack) >= 2 and stack[-1] == '#' and stack[-2]!='#':
                    stack.pop()
                    stack.pop()
                    stack.append(s)
                elif stack and stack[-1] != '#':
                    stack.append(s)
                else:
                    stack.append(s)

        if preorder == stack:
            return False
        return self.isValidSerialization(",".join(stack))