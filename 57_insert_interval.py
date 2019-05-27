class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.sort()
        
        idx = 0
        while idx < len(intervals) and (intervals[idx][1] < newInterval[0] or newInterval[1] < intervals[idx][0]):
            idx += 1

        if idx == len(intervals):
            intervals.append(newInterval)
            intervals.sort()
            return intervals
            
        intervals[idx] = [min(intervals[idx][0], newInterval[0]), max(intervals[idx][1], newInterval[1])]
        while idx < len(intervals) - 1:
            current, next_interval = intervals[idx], intervals[idx + 1]
            if next_interval[0] - current[1] <= 0:
                intervals[idx][1] = max(intervals[idx][1], next_interval[1])
                del intervals[idx + 1]
            else:
                idx += 1

        return intervals

if __name__ == "__main__":
    print Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])