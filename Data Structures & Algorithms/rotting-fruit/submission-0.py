class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if(nr<0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc]!=1 ):
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr,nc))
            time+=1
        if fresh == 0:
            return time
        return -1