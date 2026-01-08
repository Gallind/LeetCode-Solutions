class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        boolA = []
        boolB = []
        boolC = []
        a1, b1, c1 = a, b, c
        while a > 0:
            boolA.append(a & 1 == 1)
            a >>= 1
        while b > 0:
            boolB.append(b & 1 == 1)
            b >>= 1
        while c > 0:
            boolC.append(c & 1 == 1)
            c >>= 1
        a, b, c = a1, b1, c1
        max_len = max(len(boolA), len(boolB), len(boolC))
        boolA.extend([False] * (max_len - len(boolA)))
        boolB.extend([False] * (max_len - len(boolB)))
        boolC.extend([False] * (max_len - len(boolC)))
        boolA = boolA[::-1]
        boolB = boolB[::-1]
        boolC = boolC[::-1]
        print(f"a - {a} = {boolA}\nb - {b} = {boolB}\nc - {c} = {boolC}")
        counter = 0
        for i, bit in enumerate(boolC):
            if not bit:
                counter += boolA[i] + boolB[i]
            elif not boolA[i] and not boolB[i]:
                counter += 1
        return counter
