class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        if num_len <= 1:
            return num_len

        i = 0
        j = 1
        while j < num_len:
            if nums[j] != nums[j-1]:
                i += 1
                nums[i] = nums[j]
            j+= 1

        return i + 1 

        
if __name__ == "__main__":
    print Solution().removeDuplicates([-1,0,0,0,0,3,3])