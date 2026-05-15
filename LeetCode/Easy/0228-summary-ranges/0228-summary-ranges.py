class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges_lst = []
        start = end = None
        if not nums: return []
        for num in nums:
            if start == None:
                start = end = num
            elif end == num - 1:
                end = num
            else:
                if start == end:
                    ranges_lst.append(str(start))
                else:
                    ranges_lst.append(str(start) + "->" + str(end))
                start = end = num
        if start == end:
            ranges_lst.append(str(start))
        else:
            ranges_lst.append(str(start) + "->" + str(end))
        return ranges_lst