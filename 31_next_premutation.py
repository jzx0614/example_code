class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while(start < end):
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        nums_len = len(nums)
        idx = nums_len - 2
        while idx >= 0 and nums[idx] >= nums[idx+1]:
            idx -= 1

        if (idx >= 0):
            swap_value = nums[idx]
            j  = nums_len - 1
            while j > 0 and nums[j] <= swap_value:
                j -= 1
            nums[idx], nums[j] = nums[j], swap_value

        reverse(idx + 1 , nums_len -1)
        print nums



if __name__ == "__main__":
    Solution().nextPermutation([1,2,3])
    Solution().nextPermutation([3,2,1])
    Solution().nextPermutation([1,1,5])