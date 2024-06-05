class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0: return True
        count = 0
        for idx, value in enumerate(flowerbed):
            if value == 1: continue

            pre = 0 if idx == 0 else flowerbed[idx-1]
            next = 0 if (idx + 1 == len(flowerbed)) else flowerbed[idx + 1]
            if (pre or next) == 0:
                count += 1
                flowerbed[idx] = 1
                if count == n:
                    return True
                
        return False

    
if __name__ == "__main__":
    print(Solution().canPlaceFlowers([1,0,0,0,1,0,0,0,0,0,0,0], 2))
    # print(Solution().canPlaceFlowers([1,0,0,0,0,0,1], 2))
