# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = []
        q = collections.deque([root])
        while q:
            if q.count(None) == len(q):
                break
            node = q.popleft()
            if not node:
                ret.append('#')
            else:
                nextRight = node.right if node.right else None
                nextLeft = node.left if node.left else None
                q.append(nextLeft)
                q.append(nextRight)
                tmp = node.val if node else "#"
                ret.append("%d" % tmp)
        return ",".join(ret)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        q = [TreeNode(int(data.pop(0)))]
        root = q[-1]
        left = True
        while data:
            nxt = data.pop(0)
            node = None if nxt == '#' else TreeNode(int(nxt))
            if node:
                q.append(node)
            if left:
                q[0].left = node
            else:
                q[0].right = node
                q.pop(0)
            left = not left
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))