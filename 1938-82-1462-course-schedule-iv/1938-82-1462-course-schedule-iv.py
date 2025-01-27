class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        is_prerequisites=[[False]*numCourses for _ in range(numCourses)]
        for edge in prerequisites:
            is_prerequisites[edge[0]][edge[1]]=True
        for intermediate in range(numCourses):
            for source in range(numCourses):
                for target in range(numCourses):
                    is_prerequisites[source][target]=is_prerequisites[source][target] or (is_prerequisites[source][intermediate] and is_prerequisites[intermediate][target])
        result=[]
        for query in queries:
            result.append(is_prerequisites[query[0]][query[1]])
        return result