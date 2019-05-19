class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for _ in xrange(9)]
        column = [set() for _ in xrange(9)]
        boxs = [[set() for _ in xrange(3)] for _ in xrange(3)]

        def push_set(x, y, num):
            row[x].add(num)
            column[y].add(num)
            boxs[x/3][y/3].add(num)

        def pop_set(x, y, num):
            row[x].remove(num)
            column[y].remove(num)
            boxs[x/3][y/3].remove(num)

        def used_set(x, y):
            return row[x] | column[y] | boxs[x/3][y/3]

        fill_list = []
        for x in xrange(9):
            for y in xrange(9):
                num = board[x][y]
                if num == '.': 
                    fill_list.append((x, y))
                    continue
                push_set(x, y, num)
        
        all_set = set('123456789')
        def fill_num(fill_list):
            if len(fill_list) == 0:
                print 'finish....'
                return True

            x, y = min(fill_list, key=lambda arg: len(all_set - used_set(arg[0], arg[1])))
            fill_list.remove((x,y))

            new_set = all_set - used_set(x,y)

            for num in new_set:
                board[x][y] = num
                push_set(x, y, num)

                if fill_num(fill_list):
                    return True

                pop_set(x, y, num)
            
            fill_list.insert(0, (x,y))
            return False


        fill_num(fill_list)
        for x in board:
            print x

if __name__ == "__main__":
    # Solution().solveSudoku([
    #     ["5","3",".",".","7",".",".",".","."],
    #     ["6",".",".","1","9","5",".",".","."],
    #     [".","9","8",".",".",".",".","6","."],
    #     ["8",".",".",".","6",".",".",".","3"],
    #     ["4",".",".","8",".","3",".",".","1"],
    #     ["7",".",".",".","2",".",".",".","6"],
    #     [".","6",".",".",".",".","2","8","."],
    #     [".",".",".","4","1","9",".",".","5"],
    #     [".",".",".",".","8",".",".","7","9"]
    # ])

    Solution().solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]])
