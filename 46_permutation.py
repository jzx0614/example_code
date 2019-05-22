class Solution(object):    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.output = []
        self.stack = []
        def dfs(num_list):
            print num_list, self.stack
            if not num_list:
                self.output.append(self.stack[:])
            for idx, n in enumerate(num_list):
                self.stack.append(n)
                dfs(num_list[:idx] + num_list[idx+1:])
                self.stack.pop()
        dfs(nums)
        return self.output

if __name__ == "__main__":
    print Solution().permute([1,2,3])