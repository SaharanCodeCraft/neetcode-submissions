class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0" or (r,c) in visited:
                    continue
                islands += 1
                queue = deque()
                queue.append((r,c))
                visited.add((r,c))

                while queue:
                    row,col = queue.popleft()
                    directions = [
                        (1,0),
                        (-1,0),
                        (0,1),
                        (0,-1)
                    ]
                    for dr, dc in directions:
                        nr = row + dr
                        nc = col + dc
                        if(0<=nr<rows and 0<=nc<cols and grid[nr][nc] == "1" and (nr,nc) not in visited):
                            queue.append((nr,nc))
                            visited.add((nr,nc))
        return islands
