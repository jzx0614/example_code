class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        # print(points)
        ans, end = 0, points[0][0] - 1
        for p in points:
            if p[0] <= end:
                continue
            ans += 1
            end = p[1]
        return ans
    
if __name__ == "__main__":
    # print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    # print(Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
    print(Solution().findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))

    