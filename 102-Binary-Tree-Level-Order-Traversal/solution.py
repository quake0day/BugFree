# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        q = [(root, 0)]
        while q:
            node, level = q.pop()
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)

            if node.right:
                q.append((node.right, level+1))
            if node.left:
                q.append((node.left, level+1))
        return res