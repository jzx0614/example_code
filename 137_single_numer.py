class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_map = {}
        for value in nums:
            num_map[value] = num_map.get(value, 0) + 1 

            if num_map[value]:
                del num_map[value]

        return num_map.popitem()[0]

if __name__ == "__main__":
    print Solution().singleNumber([0,1,0,1,0,1,99])