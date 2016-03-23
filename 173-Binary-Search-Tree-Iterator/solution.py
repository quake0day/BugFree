# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.candidate = []
        self.pushIn(root)
    
    def pushIn(self, root):
        while root:
            self.candidate.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.candidate

    def next(self):
        """
        :rtype: int
        """
        node = self.candidate.pop()
        self.pushIn(node.right)
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())