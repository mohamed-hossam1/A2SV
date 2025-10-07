# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        can = [[False] * numCourses for i in range(numCourses)]
        
        
        for pre, cou in prerequisites:
            can[pre][cou] = True

        for i in range(numCourses): 
            for j in range(numCourses): 
                for k in range(numCourses):
                    if can[j][i] == True and can[i][k] == True:
                        can[j][k] = True

        return [can[pre][cour] for pre, cour in queries]