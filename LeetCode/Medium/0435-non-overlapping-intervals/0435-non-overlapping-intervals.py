class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        l = len(intervals)
        if l <= 1: return 0
        inter = sorted(intervals, key=lambda x: x[1])
        bCheck = inter[0][1]
        countIn = 1
        for i in range(1, l):
            a, b = inter[i]
            if a >= bCheck:
                bCheck = b
                countIn += 1
        return l - countIn
