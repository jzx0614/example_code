class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total_len = len(nums)
        if total_len <= 1:
            return 0

        step = [0] + [1e9] * (len(nums)-1)
        max_disance = 0
        for idx, n in enumerate(nums):
            if idx + n >= total_len -1:
                return step[idx] + 1
            if idx + n <= max_disance:
                continue

            for k in xrange(idx+1, idx+n+1):
                step[k] = min(step[k], step[idx] + 1)

            max_disance = n + idx

        return step[-1]
if __name__ == "__main__":
    # print Solution().jump([1,2,3])
    # print Solution().jump([2,3,1,1,4])
    # print Solution().jump([0])
    # print Solution().jump([6,7,4,3,2,0,9,8,9,9,9,6,8,3,7,5,3,3,5])
    print Solution().jump([6,7,4,3,2,0,9,8,9,9,9,6,8,3,7,5,3,3,5,3,7,2,1,3,9,2,7,0,0,9,0,6,6,4,9,8,6,0,9,5,0,0,4,8,5,3,5,8,6,1,4,5,5,5,1,6,7,8,6,9,8,8,7,6,2,6,7,8,9,8,6,9,8,2,9,3,5,5,1,1,8,7,6,5,3,7,1,2])