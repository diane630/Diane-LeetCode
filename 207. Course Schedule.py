import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         prereq_to_course = collections.defaultdict(list)
#         for (course, prereq) in prerequisites:
#             prereq_to_course[prereq].append(course)
        
#         visited = set()
#         checked = set()
#         def is_acyclic(course: int) -> bool:
#             # backtrack, if vist a node twice, then cyclic
#             if course in checked:
#                 return True
#             if course in visited:
#                 return False
#             visited.add(course)
#             for children in prereq_to_course[course]:
#                 if not is_acyclic(children):
#                     return False
#             visited.remove(course)
#             checked.add(course)
#             return True
        
#         for course_i in range(numCourses):
#             if not is_acyclic(course_i):
#                 return False
#         return True
            
        prereq_to_course = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for (course, prereq) in prerequisites:
            prereq_to_course[prereq].append(course)
            indegree[course] += 1
        
        # print(indegree)
        # print(prereq_to_course)
        
        def remove_edge(course):
            for next_course in prereq_to_course[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    remove_edge(next_course)
        q = []
        for course_i in range(numCourses):
            if indegree[course_i] == 0:
                q.append(course_i)
        for course_i in q:            
            remove_edge(course_i)
                
        # print(indegree)

        for course_i in range(numCourses):
            if indegree[course_i] > 0:
                return False
        return True
        
        