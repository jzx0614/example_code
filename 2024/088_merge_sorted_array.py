class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
 
        while n > 0:
            idx = m + n - 1
            if m > 0 and nums1[m-1] > nums2[n-1]:
                nums1[idx], nums1[m-1] = nums1[m-1], nums1[idx]
                m -= 1
            else:
                nums1[idx] =  nums2[n-1]
                n -= 1

            print(nums1, nums2)
        print(nums1)
            
if __name__ == "__main__":
    # Solution().merge([4,5,6,0,0,0], 3, [1, 2, 3], 3)
    Solution().merge([2, 0], 1, [1], 1)