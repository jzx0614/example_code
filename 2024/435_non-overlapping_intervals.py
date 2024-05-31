class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        sort_interval = sorted(intervals, key= lambda item: item[1])
        count = 0
        end = sort_interval[0][0]
        for item in sort_interval:
            # print(item, end, count)
            if item[0] < end:
                count += 1
                continue
            end = item[1]
         
        return count
    
if __name__ == "__main__":
    print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
    print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(Solution().eraseOverlapIntervals([[1,2],[2,3]]))
    