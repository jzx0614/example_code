class Solution(object):
    def maxSubArray(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ans = dp = nums[0]
        
        for idx in range(1, len(nums)):
            dp = max(dp + nums[idx], nums[idx])
            max_ans = max(dp, max_ans)
            print(idx, "max", max_ans, "dp", dp)

        return max_ans 



if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))