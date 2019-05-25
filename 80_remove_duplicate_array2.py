class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 1
        delete_count = 0

        for idx in range(len(nums)-2, -1, -1):
            if nums[idx] == nums[idx+1]:
                if count == 2:
                    del nums[idx]
                    delete_count += 1
                else:
                    count += 1
            else:
                count = 1
        print nums
        return len(nums)

if __name__ == "__main__":
    print Solution().removeDuplicates([1,2,2,2])