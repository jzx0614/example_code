class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        self.result = "("
        def dfs(l_num, r_num):
            if l_num == 0 and r_num == 0 :
                output.append(self.result)
                return
            if l_num > 0:
                self.result += '('
                dfs(l_num - 1, r_num)
                self.result = self.result[:-1]
            if l_num < r_num:
                self.result += ')'
                dfs(l_num, r_num - 1)
                self.result = self.result[:-1]

        dfs(n-1, n)
        return output

if __name__ == "__main__":
    print Solution().generateParenthesis(3)