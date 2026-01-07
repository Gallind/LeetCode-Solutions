class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for n in arr:
            if n not in count: count[n] = 0
            count[n] += 1
        return len(count) == len(set(count.values()))