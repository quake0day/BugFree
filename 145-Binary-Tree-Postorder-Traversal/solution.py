# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        postorder = []
        stack = [root]
        
        while len(stack):
            if root.left == None and root.right == None:
                postorder.append(root.val)
                root = stack.pop()
                if root.left == None:
                    root.right = None
                else:
                    root.left = None
            elif root.left:
                stack.append(root)
                root = root.left
            elif root.right:
                stack.append(root)
                root = root.right
        return postorder
        