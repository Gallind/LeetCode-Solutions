class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1: return 0
        inter = sorted(intervals, key=lambda x: x[1])
        print(inter)
        bCheck = inter[0][1]
        inter = inter[1:]
        countIn = 1
        for a, b in inter:
            if a >= bCheck:
                bCheck = b
                countIn += 1
        return len(intervals) - countIn
