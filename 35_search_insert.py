class Solution(object):
    def searchInsert(self, nums, target):
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
            
            if target < nums[start]:
                return start
            if target > nums[end]:
                return end + 1
            if nums[start] <= target < nums[mid]:
                r = binary_search(start, mid - 1, target) 
                return start + 1 if r == -1 else r
            if nums[mid] < target <= nums[end]:
                r =  binary_search(mid + 1, end, target)
                return mid + 1 if r == -1 else r    
        
        return binary_search(0, len(nums)-1, target)
        
            

if __name__ == "__main__":
    print Solution().searchInsert([1,3,5,6], 5)
    print Solution().searchInsert([1,3,5,6], 2)
    print Solution().searchInsert([1,3,5,6], 7)
    print Solution().searchInsert([1,3,5,6], 0)
