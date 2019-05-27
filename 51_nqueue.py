class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        queue_list = []
        output = []
        def dfs(row, num_list):
            if row == n:
                output.append(queue_list[:])
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
        return [['.' * queen + 'Q' +  '.' * (n-queen-1) for queen in queen_map] for queen_map in output]

if __name__ == "__main__":
    print Solution().solveNQueens(4)