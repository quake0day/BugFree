# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root == None:
            return True
        queue = collections.deque([(root,root)])
        while (len(queue)>0):
            r1,r2 = queue.popleft()
            if r1.val != r2. val:
                return False
            if r1.left and r2.right:
                queue.append((r1.left,r2.right))
            elif not r1.left and r2.right or r1.left and not r2.right:
                return False
            if r2.left and r1.right:
                queue.append((r1.right,r2.left))
            elif not r1.right and r2.left or r1.right and not r2.left:
                return False
        return True
                

            