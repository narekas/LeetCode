class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)
            
        visited = set()
        
        def dfs(i):
            if not graph[i]:
                return True
            if i in visited:
                return False
            visited.add(i)
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited.remove(i)
            return True
        
        for i in range(numCourses):
            visited = set()
            if not dfs(i):
                return False
            else:
                graph[i] = []
        return True
