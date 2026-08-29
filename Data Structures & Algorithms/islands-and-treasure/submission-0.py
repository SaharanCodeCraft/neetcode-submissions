class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        distance = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == -1 or (nr,nc) in visited):
                        continue
                    grid[nr][nc] = distance + 1
                    queue.append((nr,nc))
                    visited.add((nr,nc))
            distance += 1