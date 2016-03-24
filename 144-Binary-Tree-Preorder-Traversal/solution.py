# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            node = q.pop()
            res.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return res
            
            
            