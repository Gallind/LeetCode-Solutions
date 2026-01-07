class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        sum_alts = 0
        for alt in gain:
            sum_alts += alt
            if sum_alts > highest: highest = sum_alts
        return highest