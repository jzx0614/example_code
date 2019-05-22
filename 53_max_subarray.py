class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = pre_value = nums[0]
        for idx, n in enumerate(nums):
            if idx == 0: continue
            pre_value = max(pre_value + n, n)
            max_value = max(max_value, pre_value)
        return max_value

if __name__ == "__main__":
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])