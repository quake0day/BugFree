# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        resPos = []
        resNeg = []
        q = collections.deque([[root,0]])
        while q:
            root, pos = q.popleft()
            if root:
                if pos >= 0:
                    if len(resPos) <= pos:
                        resPos.append([])
                    resPos[pos].append(root.val)
                elif pos < 0:
                    negPos = -1 - pos
                    if len(resNeg) <= negPos:
                        resNeg.append([])
                    resNeg[negPos].append(root.val)
                
                q.append([root.left, pos-1])
                q.append([root.right, pos+1])
                
        res = resNeg[::-1] + resPos
        return res
        