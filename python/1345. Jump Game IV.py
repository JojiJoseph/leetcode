class Solution:
    def minJumps(self, arr: List[int]) -> int:
        finalized = set()
        n = len(arr)
        dist = [inf]*n
        neighbours = defaultdict(list)
        for i, item in enumerate(arr):
            neighbours[item].append(i)
        q = deque()
        q.append(0)
        dist[0] = 0
        while len(q):
            node = q.popleft()
            finalized.add(node)
            if node == n-1:
                return dist[-1]
            if node-1 >= 0 and (node-1) not in finalized:
                dist[node-1] = dist[node] + 1
                finalized.add(node-1)
                q.append(node-1)
            if node + 1 < n and (node+1) not in finalized:
                dist[node+1] = dist[node] + 1
                finalized.add(node+1)
                q.append(node+1)
                
            for next_node in neighbours[arr[node]]:
                if next_node != node and next_node not in finalized:
                    dist[next_node] = dist[node] + 1
                    finalized.add(next_node)
                    q.append(next_node)
            neighbours[arr[node]].clear()
        return dist[-1]
