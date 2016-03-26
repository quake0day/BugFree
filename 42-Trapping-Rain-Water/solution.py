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
        
        # scan from left to right, find the pivots
        # the array should be an non-decreasing array
        # e.g. [1,3,5,5,8] 1 < 3 < 5 = 5 < 8
        for i in xrange(len(height) - 1):
            if height[i] >= curMax:
                curMax = height[i]
                pivots.append(height[i])
                
        # scan from right to left, find the pivots
        # just like the above
        curMax = 0
        newpivots = []
        for j in xrange(len(height)-1, -1, -1):
            if height[j] >= curMax:
                curMax = height[j]
                newpivots.append(height[j])
        # merge left->right and right -> left using deque
        # cancel the overlap part 
        # e.g l->r [1,2,3,5,5] r->l [2, 3, 5,5]
        # final_res = [1,2,3,5,5,2,3]
        newpivots = collections.deque(newpivots[::-1])
        while newpivots and newpivots[0] == pivots[-1]:
            newpivots.popleft()
        pivots = pivots + list(newpivots)

        H = 0
        water = 0
        tmp = []
        # scan from left to right
        # try to find the pivot and calculate the water 
        # using the min H
        for k in xrange(len(height)-1, -1, -1):
            if pivots and height[k] == pivots[-1]:
                minH = min(H, height[k])
                water += sum(map(lambda x: max(minH-x,0), tmp))
                H = pivots.pop()
                tmp = []
            else:
                tmp.append(height[k])
        return water