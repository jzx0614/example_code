class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        if len(nums) == 1: 
            return True
        pre = float("-inf")
        use_ignore = False
        for idx in range(len(nums) - 1):
            # print(use_ignore, idx, "(pre/idx/idx+1)", pre, nums[idx], nums[idx+1])
            if (nums[idx] > nums[idx+1]):
                if use_ignore:
                    return False

                if pre > nums[idx+1]:
                    nums[idx + 1] = nums[idx]

                use_ignore = True
                continue
            pre = nums[idx]
        
        return True
        
if __name__ == "__main__":
    # print(Solution().checkPossibility([5,7,1,8]))
    print(Solution().checkPossibility([4, 2, 3, 4, 5, 6]))