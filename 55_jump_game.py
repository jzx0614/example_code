class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_distance = 0 
        step = [True] + [False] * (len(nums) - 1)
        for idx, n in enumerate(nums):
            if not step[idx] or n + idx <= max_distance: continue
            if  n + idx >= len(nums) -1:
                return True

            for i in xrange(idx+1,idx+n+1):
                step[i] = True
            max_distance = n + idx
        print step
        return step[-1]

if __name__ == "__main__":
    # print Solution().canJump([3,2,1,0,4])
    print Solution().canJump([1,2,3])