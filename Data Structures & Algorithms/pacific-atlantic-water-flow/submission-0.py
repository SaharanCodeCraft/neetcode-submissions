class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r,c,visit, prevheight):
            if (r<0 or r >= rows or c <0  or c >= cols or (r,c) in visit or heights[r][c] < prevheight):
                return 
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit , heights[r][c])
            dfs(r, c+1, visit,heights[r][c])
            dfs(r, c-1,visit,heights[r][c])
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atlantic,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atlantic, heights[r][cols-1])
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result