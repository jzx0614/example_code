class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(start, end, target):
            if start > end:
                return -1

            mid = (start + end) / 2
            if nums[mid] == target:
                return mid

            if nums[start] <= target < nums[mid]:
                return binary_search(start, mid - 1, target)
            if nums[mid] < target <= nums[end]:
                return binary_search(mid + 1, end, target)
            if nums[mid] > nums[end]:
                return binary_search(mid + 1, end, target)
            else:
                return binary_search(start, mid - 1, target)
        
        return binary_search(0, len(nums)-1, target)
            

if __name__ == "__main__":
    print Solution().search([1, 3], 3)