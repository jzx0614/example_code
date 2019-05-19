class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(start, end, target):
            # print start, end
            if start > end:
                return -1

            mid = (start + end) / 2
            if nums[mid] == target:
                return mid

            if nums[start] <= target < nums[mid]:
                return binary_search(start, mid - 1, target)
            if nums[mid] < target <= nums[end]:
                return binary_search(mid + 1, end, target)
            
            return -1
        
        idx = binary_search(0, len(nums)-1, target)
        if idx == -1:
            return [-1, -1]

        left = right = idx
        while left > 0 and nums[left] == nums[left -1]: left -= 1
        while right < len(nums)-1 and nums[right] == nums[right + 1]: right += 1

        return [left, right]
            

if __name__ == "__main__":
    print Solution().searchRange([1], 1)
    # print Solution().searchRange([5,7,7,8,8,10], 8)
    # print Solution().searchRange([5,7,7,8,8,10], 6)