from collections import deque

class RecentCounter:

    def __init__(self):
        self.count_q = deque()
        self.current_time = 0

    def ping(self, t: int) -> int:
        self.current_time = t
        self.count_q.append(t)
        while self.count_q[0] < self.current_time - 3000:
            self.count_q.popleft()
        return len(self.count_q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)