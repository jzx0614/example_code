class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        stack = []
        def dfs(num_list):
            if not num_list:
                return
            for idx, value in enumerate(num_list):
                stack.append(value)
                output.append(stack[:])
                dfs(num_list[idx+1:])
                stack.pop()
        dfs(nums)
        return output
if __name__ == "__main__":
    print Solution().subsets([1,2,3])