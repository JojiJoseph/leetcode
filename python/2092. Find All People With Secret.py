from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x: x[2])
        time_arr = []
        people_with_secret= set()
        people_with_secret.add(0)
        people_with_secret.add(firstPerson)
        use_time_arr = False
        prev_time = -1
        
        def find_set(parent, item):
            if item not in parent.keys():
                parent[item] = item
            if item == parent[item]:
                return item
            else:
                parent[item] = find_set(parent, parent[item])
                return parent[item]
        
        def union_sets(parent, a, b):
            a = find_set(parent, a)
            b = find_set(parent, b)
            a, b = min(a,b), max(a,b)
            if a != b:
                parent[b] = a
        
        parent = {0:0}
        for x, y, t in meetings:
            if t != prev_time:
                if use_time_arr:
                    
                    for p1, p2 in time_arr:
                        union_sets(parent, p1,p2)
                    for p1, p2 in time_arr:
                        if find_set(parent, p1) in people_with_secret or find_set(parent, p2) in people_with_secret:
                            people_with_secret.add(p1)
                            people_with_secret.add(p2)
                time_arr = []
                use_time_arr = False
                prev_time = t
                parent = {0:0}
            if x in people_with_secret or y in people_with_secret:
                parent[x] = 0
                parent[y] = 0
                people_with_secret.add(x)
                people_with_secret.add(y)
                use_time_arr = True
            time_arr.append([x,y])
        if use_time_arr:
                    for p1, p2 in time_arr:
                        union_sets(parent, p1,p2)
                    for p1, p2 in time_arr:
                        if find_set(parent, p1) in people_with_secret or find_set(parent, p2) in people_with_secret:
                            people_with_secret.add(p1)
                            people_with_secret.add(p2)
        return list(people_with_secret)