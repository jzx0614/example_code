class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
            
        n_list = self.grayCode(n-1)
        return n_list + [ 1<<(n-1) | value for value in n_list[::-1]]

if __name__ == "__main__":
    print Solution().grayCode(2)