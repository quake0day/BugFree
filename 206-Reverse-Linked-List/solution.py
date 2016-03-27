# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        q = collections.deque()
        q.append(head)
        if head.next:
            q.append(head.next)
        while len(q) > 1:
            node = q.pop()
            q.append(node)
            q[-1].next = q[-2]
            q.append(node.next)
            q.popleft()
        q[0].next = None
        return q[-1]
        