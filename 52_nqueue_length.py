class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue_list = []
        self.output = 0
        def dfs(row, num_list):
            if row == n:
                self.output += 1
                return

            for v_idex, value in enumerate(num_list):
                for idx, q in enumerate(queue_list):
                    if (row + value == idx + q) or (row - value == idx - q):
                        break
                else:
                    queue_list.append(value)
                    dfs(row+1, num_list[:v_idex] + num_list[v_idex+1:])
                    queue_list.pop()

        dfs(0, range(n))
        
        return self.output