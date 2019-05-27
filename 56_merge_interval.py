class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        idx = 0
        while idx < len(intervals) - 1:
            current, next_interval = intervals[idx], intervals[idx + 1]
            if next_interval[0] - current[1] <= 0:
                intervals[idx][1] = max(next_interval[1], current[1])
                del intervals[idx + 1]
            else:
                idx += 1
        
        return intervals
if __name__ == "__main__":
    print Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])