class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        q.append(start)
        while len(q):
            idx = q.popleft()
            if arr[idx] == -1:
                continue
            if arr[idx] == 0:
                return True
            
            if idx+arr[idx] < len(arr):
                q.append(idx+arr[idx])
            if idx-arr[idx] >= 0:
                q.append(idx-arr[idx])
            arr[idx] = -1 # visited
        return False
