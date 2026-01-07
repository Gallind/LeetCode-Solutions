class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # planted_sum = sum(flowerbed)
        if n == 0: return True
        l = len(flowerbed)
        if l == 0: return False
        possible_plants = 0
        for i in range(l):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) \
                and (i == l - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                possible_plants += 1
        return possible_plants >= n

        #     if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
        #         flowerbed[i] = 1
        #         possible_plants += 1
        # if l > 1 and flowerbed[0] == flowerbed[1] == 0:
        #     flowerbed[0] = 1
        #     possible_plants += 1
        # if l > 1 and flowerbed[l - 2] == flowerbed[l - 1]:
        #     flowerbed[l - 1] = 1
        #     possible_plants += 1
        # if l == 1 and flowerbed[0] == 0:
        #     flowerbed[0] = 1
        #     possible_plants += 1
        return possible_plants >= n
        