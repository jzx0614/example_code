class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        move_idx = 0
        for idx, value in enumerate(nums):
            if value != 0:
                nums[move_idx], nums[idx] = nums[idx], nums[move_idx]
                move_idx += 1

if __name__ == "__main__":
    print(Solution().moveZeroes([1,1,0,3,12,0, 4, 0, 0]))