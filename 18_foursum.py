class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        if nums_len < 4: return []
        result = set()
        nums.sort()
        for f_idx, first in enumerate(nums[:-3]):
            for t_idx, two in enumerate(nums[:-2]):
                if f_idx >= t_idx: continue
                th_idx, four_idx = t_idx + 1, nums_len - 1
                while th_idx < four_idx:
                    sum_value = sum([first, two, nums[th_idx], nums[four_idx]])
                    # print sum_value, first, two, nums[th_idx], nums[four_idx], f_idx, t_idx, th_idx, four_idx
                    if sum_value == target:
                        result.add((first, two, nums[th_idx], nums[four_idx]))
                        while th_idx < four_idx and nums[th_idx] == nums[th_idx+1]: 
                            th_idx += 1
                        while th_idx < four_idx and nums[four_idx] == nums[four_idx-1]: 
                            four_idx -= 1
                        th_idx, four_idx = th_idx + 1, four_idx - 1
                    elif sum_value < target:
                        th_idx += 1
                    else:
                        four_idx -= 1

        return map(list, result)

if __name__ == "__main__":
    print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)