class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def pow(x, n):
            print x, n
            if n == 0: 
                return 1
            ans = pow(x, n/2)
            ans *= ans 
            return x * ans if (n & 1) else ans

        ans = pow(x, abs(n))
        return ans if n >= 0 else 1/ans 

if __name__ == "__main__":
    # print Solution().myPow(2.0, 10)
    print Solution().myPow(2.0, -2)