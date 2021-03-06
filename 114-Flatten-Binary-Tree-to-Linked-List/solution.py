# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        q = collections.deque()
        l = collections.deque()
        q.append(root)
        while q:
            node = q.pop()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            l.append(node)
            if len(l) > 1:
                if l[-1] and l[-2]:
                    l[-1].left = None
                    l[-2].right = l[-1]
        l[0].left = None
        