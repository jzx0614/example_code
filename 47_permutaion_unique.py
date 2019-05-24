class Solution(object):    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.output = set()
        self.stack = []
        def dfs(num_list):
            if not num_list:
                self.output.add(tuple(self.stack))
            for idx, n in enumerate(num_list):
                self.stack.append(n)
                dfs(num_list[:idx] + num_list[idx+1:])
                self.stack.pop()
        dfs(nums)
        return map(list, self.output)

if __name__ == "__main__":
    print Solution().permuteUnique([1,1,2])