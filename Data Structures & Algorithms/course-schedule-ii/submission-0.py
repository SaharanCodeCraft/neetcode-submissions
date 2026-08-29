class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        output = []

        # Courses completely processed
        visit = set()

        # Courses currently in our DFS path
        cycle = set()

        def dfs(course):

            # We came back to a course in the current path
            if course in cycle:
                return False

            # Already completely processed
            if course in visit:
                return True

            # Add to current path
            cycle.add(course)

            # Check all prerequisites
            for prerequisite in preMap[course]:

                if not dfs(prerequisite):
                    return False

            # Done with this course
            cycle.remove(course)

            # Mark as completely processed
            visit.add(course)

            # Add to output
            output.append(course)

            return True

        # Try every course
        for course in range(numCourses):

            if not dfs(course):
                return []

        

        return output
        