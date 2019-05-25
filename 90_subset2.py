class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        stack = []
        nums.sort()
        def dfs(num_list):
            if not num_list:
                return
            for idx, value in enumerate(num_list):
                if idx > 0  and value == num_list[idx-1]:
                    continue
                stack.append(value)
                output.append(stack[:])
                dfs(num_list[idx+1:])
                stack.pop()
        dfs(nums)
        return output 

if __name__ == "__main__":
    print Solution().subsetsWithDup([4,4,4,1,4])