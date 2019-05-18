class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = -1
        for n in nums:
            if n == val: continue
            i += 1
            nums[i] = n
        return i + 1 

        
if __name__ == "__main__":
    print Solution().removeElement([0,1,2,2,3,0,4,2], 2)