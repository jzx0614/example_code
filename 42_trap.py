class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_idx, right_idx = 0, len(height)-1
        left_max = right_max = 0
        ans = 0
        while left_idx < right_idx:
            if  height[left_idx] < height[right_idx]:
                if left_max > height[left_idx]:
                    ans += left_max - height[left_idx]
                else:
                    left_max = height[left_idx]
                left_idx += 1
            else:
                if right_max > height[right_idx]:
                    ans += right_max - height[right_idx]
                else:
                    right_max = height[right_idx]
                right_idx -= 1
        return ans

if __name__ == "__main__":
    print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])