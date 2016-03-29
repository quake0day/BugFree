# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        q = collections.deque()
        i = 0
        while root or q:
            if root:
                q.append(root)
                root = root.left
            else:
                root = q.pop()
                i += 1
                if i == k:
                    return root.val
                root = root.right
        return -1 