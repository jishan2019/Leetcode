# 933. Number of Recent Calls

# Queue

##using deque
class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



# binary search
class RecentCounter:

    def __init__(self):
        self.nums = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.nums.append(t)
        cur_pos = len(self.nums)
        prev_pos = bisect.bisect_left(self.nums, t - 3000)
        return cur_pos - prev_pos

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)