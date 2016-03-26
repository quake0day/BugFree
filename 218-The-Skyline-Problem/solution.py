import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(buildings)
        start = map(lambda x:x[0],buildings)
        end = map(lambda x:x[1], buildings)
        height = map(lambda x: x[2], buildings)
        s_t = zip(start, height, [0] * n)
        e_t = zip(end, height, [1] * n)
        total_t = s_t + e_t
        total_t = sorted(total_t, key=lambda x:(x[0],x[2]))
        h = [0]
        res = []
        heapq.heapify(h)
        for t in total_t:
            if t[2] == 0:
                prev = heapq.nlargest(1,h)[0] if h else 0
                heapq.heappush(h, t[1])
                if prev < t[1]:
                    res.append(t[:2])
            elif t[2] == 1:
                h.remove(t[1])
                heapq.heapify(h)
                top = heapq.nlargest(1,h) if heapq.nlargest(1,h) else [0]
                if top[0] < t[1]:
                    res.append([t[0]] + top)
        return res
            