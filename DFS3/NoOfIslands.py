class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid) # assinging with row length
        self.n = len(grid[0]) # assinging with column length
        self.count = 0
        self.dirs = [[0,1],[0,-1],[1,0],[-1,0]] # setting direction array
        self.result = [] # creating result array
        for i in range(self.m):
            for j in range(self.n):
                self.island = [] # creating island empty array
                if grid[i][j] == "1": # if grid value is equal to 1
                    self.dfs(grid,i,j) # calling dfs function recursively
                    self.result.append(self.island) # appending island value to result
                    self.count +=1 # incrementing count
        return self.count # returning count
     
    def dfs(self,grid,i,j):
        if grid[i][j]=="0":
            return
        
        self.island.append((i,j)) # appending the i and j value in island array
        grid[i][j]="0" # assinging grid value to 0
        for x,y in self.dirs: # for in directions array
            nr = x+i
            nc = y+j
            if nr>=0 and nr<self.m and nc>=0 and nc<self.n: # boundary check
                self.dfs(grid,nr,nc) # calling dfs function recursively