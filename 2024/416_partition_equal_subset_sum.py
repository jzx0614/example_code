from functools import reduce

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum = reduce(lambda x, y: x + y, nums)
        if (sum & 1) == 1: return False
        w = sum // 2

        dp = [[True] + [False for _ in range(w)] for _ in range(len(nums) + 1) ]

        for i in range(len(nums)):
            for weight in range(w, nums[i] - 1, -1):
                dp[i + 1][weight] = dp[i][weight] or dp[i][weight - nums[i]]
            print(i, nums[i], dp[i+1])
        return dp[i][w]


if __name__ == "__main__":
    print(Solution().canPartition([1,5,11,5]))