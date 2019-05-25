class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        previous = start = 0
        end = x
        
        while start <= end :
            guess = (start + end) // 2
            diff = x - guess * guess
            if diff == 0:
                return guess
            elif diff < 0:
                end = guess -1
            else:
                previous = guess
                start = guess + 1
        return previous
if __name__ == "__main__":
    print Solution().mySqrt(8)