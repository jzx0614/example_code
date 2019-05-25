class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        num = range(1, n+1)
        output = []
        stack = []
        def dfs(num_list, k):
            if len(num_list) < k:
                return
            if k == 0 or not num_list:
                output.append(stack[:])
                return
            for idx, value in enumerate(num_list):
                stack.append(value)
                dfs(num_list[idx+1:], k-1)
                stack.pop()

        dfs(num, k)
        return output
if __name__ == "__main__":
    print Solution().combine(4, 2)