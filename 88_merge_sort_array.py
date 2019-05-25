class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m == 0 or nums1[m-1] < nums2[n-1]:
                max_value = nums2[n-1]
                n -= 1
            else:
                max_value = nums1[m-1]
                m -= 1
            
            nums1[m+n] = max_value
            
        print nums1

if __name__ == "__main__":
    Solution().merge([7,8,9,0,0,0],3,[1,1,1],3)