#Time_Complexity: O(mn)
#Space_Complexity: O(n)


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)    #m is the length of row
        n = len(mat[0]) #n is the length of column
        
        dirs_= [[0,1],[1,0],[0,-1],[-1,0]]  #Direction array
        q = deque() #Initialze q using deque
        
        for i in range(m):  
            for j in range(n):
                if mat[i][j] == 0:  #If mat[i][j] is 0 then append i, j into the q
                    q.append((i,j))
                else:   #Else change mat[i][j] to -1 to keep track
                    mat[i][j] = -1
                    
        dist = 0    #Initialize dist as 0
        while q:    #Continue till the q is empty
            size = len(q)   #Size is the length of the q
            dist += 1   #Increment dist by 1
            for _ in range(size):   #Continue till the size
                curr = q.popleft()  #Pop the first element in the q
                
                for x,y in dirs_:   #For x, y in drection array traverse all the neighboring elements
                    nr = x+curr[0]
                    nc = y+curr[1]
                    
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and mat[nr][nc] == -1: #Boundary check and if mat[nr][nc] is equal to -1
                        mat[nr][nc] = dist  #Change mat[nr][nc] as dist
                        q.append((nr,nc))   #Append nr, nc into the q
                        
        return mat  #Return mat