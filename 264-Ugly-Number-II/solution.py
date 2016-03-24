class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        minHeap = [2, 3, 5]
        heapq.heapify(minHeap)
        i = 0
        s = set()
        while i < n-1:
            val = heapq.heappop(minHeap)
            for k in [2,3,5]:
                if val * k not in s:
                    s.add(val*k)
                    heapq.heappush(minHeap, val*k)
            i += 1
        return val