class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, x in enumerate(nums):
            print "1", nums
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

if __name__ == "__main__":
    print Solution().firstMissingPositive([3, 2, 1, 0 ,9 , 8 ,-1])
