class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums_d = {
            '2': ['a','b','c'], '3': ['d','e','f'],
            '4': ['g','h','i'], '5': ['j','k','l'],
            '6': ['m','n','o'], '7': ['p','q','r','s'],
            '8': ['t','u','v'], '9': ['w','x','y','z'],
        }
        l = len(digits)
        sol = []

        def permRec(index, prefix_s):
            if len(prefix_s) == l:
                sol.append(prefix_s)
                return
            
            digit = digits[index]
            letters = nums_d[digit]

            for ch in letters:
                permRec(index + 1, prefix_s + ch)
        
        permRec(0, "")
        return sol







        # temp_s = ""
        # for digit1 in digits:
        #     for ch1 in nums_d[digit1]:
        #         temp_s += ch1
        #         if l >= 2:
        #             for digit2 in digits[1:]:
        #                 for ch2 in nums_d[digit2]:
        #                     temp_s += ch2
        #                     if l >= 3:
        #                         for digit3 in digits[2:]:
        #                             for ch3 in nums_d[digit3]:
        #                                 temp_s += ch3
        #                                 if l == 4:
        #                                     for ch4 in nums_d[3]:
        #                                         temp_s += ch4
        #                                 else:
        #                                     sol.append(temp_s)
        #                                     temp_s = temp_s[:-1]
        #                     else:
        #                         sol.append(temp_s)
        #                         temp_s = temp_s[:-1]
        #         else:
        #             sol.append(temp_s)
        #             temp_s = temp_s[:-1]
        #         sol.append(temp_s)
        #         temp_s = ""
        # return sol
