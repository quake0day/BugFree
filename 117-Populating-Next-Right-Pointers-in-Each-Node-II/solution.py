# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        nxt, pre = None, None
        while root or nxt:
            if root.left:
                if pre:
                    pre.next = root.left
                pre = root.left
            if root.right:
                if pre:
                    pre.next = root.right
                pre = root.right
            if not nxt and (root.left or root.right):
                nxt = root.left if root.left else root.right
            root = root.next
            if not root:
                root = root.left 
                nxt = None
                pre = None
                