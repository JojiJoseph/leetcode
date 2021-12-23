class Solution:
    def dfs(self, i, adj_list, visited, current_set, stack):
        if i in current_set:
            return False
        if visited[i]:
            return True
        visited[i] = 1
        current_set.add(i)
        for j in adj_list[i]:
            if not self.dfs(j, adj_list, visited, current_set, stack):
                return False
        stack.append(i)
        current_set.remove(i)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack = []
        adj_list = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            adj_list[b].append(a)

        visited = [0] * numCourses
        for i in range(numCourses):
            current_set = set()
            if not self.dfs(i, adj_list, visited, current_set, stack):
                return []
        return stack[::-1]
