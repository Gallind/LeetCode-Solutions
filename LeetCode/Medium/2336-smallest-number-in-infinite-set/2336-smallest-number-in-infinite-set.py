class SmallestInfiniteSet:
    SMALL = 1
    MIN = 1
    def infGen(self):
        x = self.MIN
        while True:
            while x not in self.ADDED_BACK and x < self.SMALL:
                x += 1
            yield x
            x += 1
    def __init__(self):
        self.ADDED_BACK = set()
        self.inf_set = self.infGen()
        

    def popSmallest(self) -> int:
        minimum = self.SMALL + 10
        if self.ADDED_BACK:
            minimum = min(self.ADDED_BACK)
            self.ADDED_BACK.discard(minimum)
            # return minimum
        else:
            self.SMALL += 1
            # return self.SMALL - 1
        self.MIN = min(minimum + 1, self.SMALL)
        return self.MIN - 1


    def addBack(self, num: int) -> None:
        # self.MIN = min(self.MIN, num)
        if num < self.SMALL:
            self.ADDED_BACK.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)