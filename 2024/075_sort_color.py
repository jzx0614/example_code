from functools import reduce
class Solution:
    # def sortColors(self, nums: list[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     zero_count = reduce(lambda sum, value: sum + 1 if value == 0 else sum, [0] + nums)
    #     two_count = reduce(lambda sum, value: sum + 1 if value == 2 else sum, [0] + nums)
    #     for i in range(len(nums)):
    #         if i < zero_count:
    #             nums[i] = 0
    #         elif i >= len(nums) - two_count:
    #             nums[i] = 2
    #         else:
    #             nums[i] = 1
    #     print(nums)
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_count = one_count = 0
        for value in nums:
            if value == 0:
                nums[zero_count] = 0
                zero_count += 1
            elif value == 1:
                one_count += 1


        for i in range(zero_count, len(nums)):
            nums[i] = 1 if (i - zero_count) < one_count else 2
        print(nums)

if __name__ == "__main__":
    Solution().sortColors([2,1,0,2,1,0,1,0])