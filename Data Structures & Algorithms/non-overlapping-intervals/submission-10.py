class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        i, count = 1, 0

        last_kept = intervals[0][1]

        while i < len(intervals):
            if intervals[i][0] < last_kept:
                count += 1
            else:
                last_kept = intervals[i][1]
            i += 1
        return count
                