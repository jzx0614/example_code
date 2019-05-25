class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return False

        self.row = len(board)
        self.col = len(board[0])
        direct_list = [(-1,0),(0, -1),(1, 0), (0, 1)]
        def check(i, j, word):
            if not word: return True
            if not (0 <= i < self.row and 0 <= j < self.col) or word[0] != board[i][j]:
               return False

            temp, board[i][j] = board[i][j], '#'
            for d in direct_list:
                if check(i + d[0], j+d[1], word[1:]):
                    return True
            board[i][j] = temp

        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                if check(x, y, word):
                    return True

        return False
if __name__ == "__main__":
    print Solution().exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'SEE')