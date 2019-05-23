class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if 1 in [n, m]: 
            return 1

        m, n  = m-1, n-1
        if m > n: 
            m, n = n ,m
        mul = lambda x, y: x*y
        f_m = reduce(mul, range(m+1,m+n+1))
        f_n = reduce(mul, range(1,n+1))

        return f_m / f_n

if __name__ == "__main__":
    print Solution().uniquePaths(3, 2)
    print Solution().uniquePaths(7, 3)

