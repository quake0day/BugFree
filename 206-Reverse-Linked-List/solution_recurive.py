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
        if not head or not head.next:
            return head
        return self.reverse(head, None)
    
    def reverse(self, head, prev):
        if not head:
            return prev
        tmp = head.next
        head.next = prev
        return self.reverse(tmp, head)
        