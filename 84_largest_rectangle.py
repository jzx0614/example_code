class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_value = 0
        heights.append(0)
        stack = [-1]

        for idx in xrange(len(heights)):
            while stack and heights[idx] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = idx - stack[-1] -1
                max_value = max(max_value, w * h)
            stack.append(idx)
        
        return max_value
if __name__ == "__main__":
    print Solution().largestRectangleArea([2,1,5,6,2,3])

