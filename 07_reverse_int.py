class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negtive = False
        if (x < 0) 
            x = 0 - x
            negtive = True
        
        rev = 0
        while(x > 0):
            pop = x % 10 
            x /= 10
            
            rev = rev * 10 + pop 
        
        if (negtive) rev = 0 - rev
        
        return 0 abs(rev) 
        answer = answer if answer <= 2147483647 else 0
        answer = answer if answer > -2147483648 else 0
        
        return answer
        
if __name__ == "__main__":
    print Solution().reverse(1534236469)