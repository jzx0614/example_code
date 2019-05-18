class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        nums.sort()
        # print nums
        for mid in xrange(1, len(nums)-1):
            l, r = 0 , len(nums) - 1 
            while l < mid and r > mid:
                # print "(%d, %d, %d) (%d, %d, %d)" % (nums[l], nums[mid], nums[r], l, mid, r)
                sum_value = nums[l] + nums[mid] + nums[r]
                if sum_value == 0:
                    result.add((nums[l], nums[mid], nums[r]))
                    while(l < mid and nums[l] == nums[l+1]): 
                        l += 1
                    while(mid < r and nums[r] == nums[r-1]): 
                        r -= 1
                    l, r = l+1, r-1
                elif sum_value < 0:
                    l += 1
                else:
                    r -= 1
        return map(list, result)

if __name__ == "__main__":
    print Solution().threeSum([-1,0,1,2,-1,-4])
    print Solution().threeSum([0,0,0,0])
    print Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])