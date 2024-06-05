class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        l, r = 1, x // 2
        while l <= r:
            mid = (l + r) // 2
            sqrt_mid = mid * mid
            if sqrt_mid == x:
                return mid
            elif sqrt_mid < x:
                l = mid + 1
            else:
                r = mid - 1
        
        return r
            
if __name__ == "__main__":
    print(Solution().mySqrt(8))