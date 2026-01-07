class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max1 = max(candies)
        sol = []
        for kid in candies:
            sol.append(kid + extraCandies >= max1)
        return sol
                
        