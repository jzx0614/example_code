class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
              r -=1
            else:
              l += 1
        return max_area

if __name__ == "__main__":
    print Solution().maxArea([1,8,6,2,5,4,8,3,7])