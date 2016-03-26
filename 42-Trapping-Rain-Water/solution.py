import collections
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height = [0] + height + [0]
        pivots = []
        curMax = 0

        for i in xrange(len(height) - 1):
            if height[i] >= curMax:
                curMax = height[i]
                pivots.append(height[i])
        curMax = 0
        newpivots = []
        for j in xrange(len(height)-1, -1, -1):
            if height[j] >= curMax:
                curMax = height[j]
                newpivots.append(height[j])
        newpivots = collections.deque(newpivots[::-1])
        while newpivots and newpivots[0] == pivots[-1]:
            newpivots.popleft()
        pivots = pivots + list(newpivots)

        H = 0
        water = 0
        tmp = []
        for k in xrange(len(height)-1, -1, -1):
            if pivots and height[k] == pivots[-1]:
                minH = min(H, height[k])
                water += sum(map(lambda x: max(minH-x,0), tmp))
                H = pivots.pop()
                tmp = []
            else:
                tmp.append(height[k])
        return water