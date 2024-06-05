class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            print(l, r, "value", nums[l], nums[r], mid)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        print(l, r)
        return nums[l]