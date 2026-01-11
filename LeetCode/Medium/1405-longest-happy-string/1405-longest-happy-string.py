import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0: heapq.heappush(max_heap, (-a, 'a'))
        if b > 0: heapq.heappush(max_heap, (-b, 'b'))
        if c > 0: heapq.heappush(max_heap, (-c, 'c'))

        sol = ""
        while max_heap:
            count, ch = heapq.heappop(max_heap)
            if len(sol) >= 2 and sol[-1] == sol[-2] == ch:
                if not max_heap: return sol
                count2, ch2 = heapq.heappop(max_heap)
                sol += ch2
                count2 += 1
                if count2 < 0: heapq.heappush(max_heap, (count2, ch2))
                heapq.heappush(max_heap, (count, ch))
            else:
                sol += ch
                count += 1
                if count < 0: heapq.heappush(max_heap, (count, ch))
        return sol
