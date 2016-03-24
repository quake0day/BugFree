import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.higher = []
        self.lower = []
        heapq.heapify(self.higher)
        heapq.heapify(self.lower)
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.higher or self.higher[0] < num:
            heapq.heappush(self.higher, num)
        else:
            heapq.heappush(self.lower, -1 * num)
        self.adjust()
    
    def adjust(self):
        if len(self.higher) - len(self.lower) > 1:
            heapq.heappush(self.lower, -1 * heapq.heappop(self.higher))
        elif len(self.lower) - len(self.higher) > 1:
            heapq.heappush(self.higher, -1 * heapq.heappop(self.lower))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.higher) == len(self.lower):
            return (float(self.higher[0]) + float(-1 * self.lower[0])) / 2
        elif len(self.higher) == len(self.lower) + 1:
            return self.higher[0]
        elif len(self.higher) + 1 == len(self.lower):
            return (-1) * self.lower[0]