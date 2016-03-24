# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        q = collections.deque()
        while root or q:
            if root:
                q.append(root)
                root = root.left
            else:
                root = q.pop()
                res.append(root.val)
                root = root.right
        return res
                