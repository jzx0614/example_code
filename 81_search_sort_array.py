class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(start, end, target):
            if start > end:
                return False

            mid = (start + end) / 2

            while start < mid and nums[start] == nums[mid]:
                 start += 1
            while mid < end and nums[end] == nums[mid]:
                 end -= 1

            if target in [nums[mid], nums[start], nums[end]]:
                return True
                
            if nums[start] <= target < nums[mid]:
                return binary_search(start + 1, mid - 1, target)
            if nums[mid] < target <= nums[end]:
                return binary_search(mid + 1, end - 1 , target)
            if nums[mid] > nums[end]:
                return binary_search(mid + 1, end, target)
            else:
                return binary_search(start, mid - 1, target)
        
        return binary_search(0, len(nums)-1, target)
            

if __name__ == "__main__":
    print Solution().search([1,1,3,1], 3)
    print Solution().search([3,1,1], 3)
    # print Solution().search([6,6,6,6,6,6,6,1,6,6,6,6], 4)
