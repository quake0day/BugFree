# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        minHeap = [(node.val, node) for node in lists if node]
        head = ListNode(0)
        p = head
        heapq.heapify(minHeap)
        while minHeap:
            _, node = heapq.heappop(minHeap)
            if node.next:
                heapq.heappush(minHeap, (node.next.val, node.next))
            p.next = node
            p = p.next
        return head.next
        