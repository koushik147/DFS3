#TimeComplexity: O(mn)
#SpaceComplexity: O(mn)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dirs = [[0,1],[1,0],[-1,0],[0,-1]] # setting direction array
        self.colorTBC = image[sr][sc] # assigning image value to colorTBC
        self.fillWith = color # assinging color to fillwith
        self.image = image
        self.m = len(image) # storing row length
        self.n = len(image[0]) # storing column length
        
        if self.colorTBC == color: # if color is equal to colorTBC
            return image # returning image grid
        
        self.dfs(sr,sc) # calling dfs function recursively
        return self.image # returing image
    
    def dfs(self,sr,sc):
        self.image[sr][sc] = self.fillWith # assigning fillwith to image grid
        for x,y in self.dirs: # for in direction array
            nr = x+sr
            nc = y+sc
            if nr>=0 and nr<self.m and nc>=0 and nc<self.n and self.image[nr][nc] == self.colorTBC: # boundary check
                self.dfs(nr,nc) # calling dfs function recursively
                
        return
