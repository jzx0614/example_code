class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx_hash = {}
        for idx, num in enumerate(numbers, 1):
            if idx_hash.has_key(num):
                return [idx_hash[num], idx]
            else:
                idx_hash[target-num] = idx

if __name__ == "__main__":
    print Solution().twoSum([2,7,11,15], 9)