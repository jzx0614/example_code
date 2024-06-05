class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]

        l, r = 0, len(nums) - 1
        while l < r:
            idx = (l + r) // 2
            if idx % 2 == 1:
                idx -= 1
            # print("index", l, idx, r, "value", nums[l], nums[idx], nums[r])
            if nums[idx] == nums[idx + 1]: #  idx < ans
                l = idx + 2
            else:
                r = idx
            
        return r
if __name__ == "__main__":
    print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))