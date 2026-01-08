class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_score = 0
        min_heap = []
        pairs = zip(nums2, nums1)
        pairs_s = sorted(list(pairs), reverse=True)
        nums1 = [b for (a, b) in pairs_s]
        nums2 = [a for (a, b) in pairs_s]

        l = len(nums1)
        if k >= l: return sum(nums1) * nums2[l - 1]
        
        prefix_sum = 0
        for a, b in zip(nums1, nums2):
            prefix_sum += a
            heappush(min_heap, a)
            if len(min_heap) == k:
                max_score = max(max_score, prefix_sum * b)
                prefix_sum -= heappop(min_heap)
        return max_score

