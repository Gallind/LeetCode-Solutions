# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    START = 1
    END = -1
    def guessNumber(self, n: int) -> int:
        self.END = n
        guess_n = (self.START + self.END) // 2
        while guess(guess_n) != 0:
            mode = guess(guess_n)
            if mode > 0:
                self.START = guess_n + 1
            elif mode < 0:
                self.END = guess_n - 1
            guess_n = (self.START + self.END) // 2
        return guess_n

        