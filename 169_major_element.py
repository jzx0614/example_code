class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        c =  collections.Counter(nums)
        return c.most_common(1)[0][0]

if __name__ == "__main__":
    print Solution().majorityElement([2,2,1,1,1,2,2])