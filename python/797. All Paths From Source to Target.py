from typing import List


class Solution:
    def util(self, graph, src, dst, running_path, paths):
        running_path.append(src)
        if src == dst:
            paths.append(running_path.copy())
        else:
            for next_node in graph[src]:
                self.util(graph, next_node, dst, running_path, paths)
        running_path.pop()
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        running_path = []
        paths = []
        self.util(graph, 0, len(graph)-1, running_path, paths)
        return paths
