class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newList = sorted(nums1 + nums2)
        print newList
        listLen = len(newList)
        if listLen % 2 == 1:
            return newList[listLen/2] / 1.0
        else:
            leftIdx = (listLen/2) - 1
            rightIdx = (listLen/2)
            return (newList[leftIdx] + newList[rightIdx]) / 2.0
        
        
if __name__ == "__main__":
    nums1 = [1,2,3,4,5]
    nums2 = [2,3,4,5,6,7]
    print Solution().findMedianSortedArrays(nums1, nums2)