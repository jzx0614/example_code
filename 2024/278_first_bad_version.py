# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            ans = isBadVersion(mid)
            # print(l, r, mid, ans)
            if ans:
                r = mid
            else:
                l = mid + 1
        
        # print("ans", l, r)
        return l