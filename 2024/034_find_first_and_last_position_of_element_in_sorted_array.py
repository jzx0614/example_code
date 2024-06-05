class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0: return [-1, -1]
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        print(len(nums), l, r)
        if nums[l] != target: 
            return [-1, -1]
            
        ans = [l, l]
        for idx in range(l, len(nums)):
            if nums[idx] != target: break
            ans[1] = idx
        return ans

if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,10], 8))