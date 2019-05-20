class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx in xrange(len(nums)):
            while 0 < nums[idx] <= len(nums) and nums[idx] != idx + 1 and nums[idx] != nums[nums[idx]-1]:
                nums[nums[idx]-1], nums[idx] = nums[idx], nums[nums[idx]-1]

        for idx, n in enumerate(nums):
            if idx + 1 != n:
                return idx + 1

        return len(nums) + 1


if __name__ == "__main__":
    print Solution().firstMissingPositive([])
    # print Solution().firstMissingPositive([3, 2, 1, 0 ,9 , 8 ,-1])
