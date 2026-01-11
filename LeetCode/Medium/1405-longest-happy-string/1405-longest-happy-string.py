import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if not a and not b and not c: return ""
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













        # let_dict = {
        #     'a': -a,
        #     'b': -b,
        #     'c': -c
        # }
        # for ch in let_dict:
        #     if let_dict[ch] < 0:
        #         heapq.heappush(max_heap, (let_dict[ch], ch))
        # sol = ""
        # while max_heap:
        #     top = heapq.heappop(max_heap)
        #     if len(sol) >= 2 and sol[-1] == sol[-2] == top[1]:
        #         if not max_heap: return sol
        #         second = heapq.heappop(max_heap)
        #         heapq.heappush(max_heap, top)
        #         top = second
        #     sol += top[1]
        #     if top[0] < 0: heapq.heappush(max_heap, (top[0]+1, top[1]))
        # return sol








        '''
        # if not a and not b and not c: return ""
        # let_dict = {
        #     'a': a,
        #     'b': b,
        #     'c': c
        # }
        # maxId = 'a'
        # maxNum = max(a, b, c)
        # if b == maxNum: maxId = 'b'
        # elif c == maxNum: maxId = 'c'

        # sol = ""
        # if maxNum >= 2: 
        #     sol += maxId * 2
        #     let_dict[maxId] -= 2
        # elif maxNum >= 1: 
        #     sol += maxId
        #     let_dict[maxId] -= 1
        # else: return sol
        # def add2L(let_dict, maxId):
        #     nonlocal sol
        #     print(f"{sol = }\n{let_dict = }\n{maxId = }\n{'-'*20}")
        #     (lst:=['a', 'b', 'c']).remove(maxId)
        #     maxNum = max(let_dict[lst[0]], let_dict[lst[1]])
        #     print(f"{lst = }\n{maxNum = }\n{'='*20}")
        #     if not maxNum: return
        #     if let_dict[lst[0]] == maxNum: 
        #         maxId = lst[0]
        #     else: maxId = lst[1]

        #     if maxNum >= 2: 
        #         sol += maxId * 2
        #         let_dict[maxId] -= 2
        #     elif maxNum >= 1: 
        #         sol += maxId
        #         let_dict[maxId] -= 1
        #     else: return

        #     add2L(let_dict, maxId)

        # add2L(let_dict, maxId)
        # return sol
    '''









