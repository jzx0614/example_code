class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = nums[0], nums[nums[0]] 

        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]] 

        slow = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow

if __name__ == "__main__":
    print(Solution().findDuplicate([1,3,4,2,2]))