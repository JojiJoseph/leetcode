from typing import List
from collections import deque, defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        max_bombs = 0
        n = len(bombs)
        for i, bomb in enumerate(bombs):
            for j, next_bomb in enumerate(bombs):
                if i != j and (bomb[0]-next_bomb[0])**2 + (bomb[1]-next_bomb[1])**2 <= bomb[2]**2:
                    graph[i].append(j)
                    
        for i in range(n):
            q = deque()
            q.append(i)
            visited = set()
            span = 0

            while len(q):
                current = q.popleft()
                if current in visited:
                    continue
                span += 1
                visited.add(current)
                for j in graph[current]:
                    if j not in visited:
                        q.append(j)
            max_bombs = max(max_bombs, span)
        
        return max_bombs
