from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()
        # self.start = 0
        # self.requests = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
        # self.requests.append(t)
        # while self.requests[self.start] < t - 3000:
        #     self.start += 1
        # return len(self.requests) - self.start


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)