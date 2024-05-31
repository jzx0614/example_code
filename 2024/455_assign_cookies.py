class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        for greed in g:
            while len(s) > 0:
                cookie_size = s.pop(0)
                if greed <= cookie_size:
                    result += 1
                    break
        return result
    
if __name__ == "__main__":
    print(Solution().findContentChildren([1,2,3], [3]))