class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, green = 0, len(nums)-1
        idx = 0
        while idx <= green:
            n = nums[idx]
            if n == 0:
                nums[idx], nums[red] =  nums[red], nums[idx]
                red += 1
            elif n == 2:
                nums[idx], nums[green] =  nums[green], nums[idx]
                idx, green = idx - 1, green -1

            idx += 1

        print nums

if __name__ == "__main__":
    Solution().sortColors([1, 2, 0])