#Time_Complexity: O(mn)
#Space_Complexity: O(n)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCount = 0  #Initialize freshCount as 0
        time = 0    #Initialize time as 0
        q = deque() #Initialize q using deque
        dirs_ = [[0,1],[0,-1],[1,0],[-1,0]] #Initailize direction array both horizontaly and vertically
        m = len(grid)   #M is the length of row
        n = len(grid[0])    #n is the lenght of column
        for i in range(m):  
            for j in range(n):
                if grid[i][j] == 2: #If the grid[i][j] is 2 then append it into the q
                    q.append((i,j))
                elif grid[i][j] == 1:   #Else if the grid[i][j] is 1 increment freshCount by 1
                    freshCount += 1
                    
                    
        while q and freshCount != 0:    #Continue till the q is empty and freshCount is not equal to 0
            time+=1 #Add time by 1
            size = len(q)   #Size is the length of q
            for _ in range(size):   #Continue till the size
                curr = q.popleft()  #Pop the first element in the q using popleft and store it in curr

                for r,c in dirs_:   #For r,c in the direction array traverse throught the neighboring elements
                    nr = r+curr[0]
                    nc = c+curr[1]

                    if nr >= 0 and nr < m and nc >= 0 and nc < n:   #Boundary check
                        if grid[nr][nc] == 1:   #If the grid[nr][nc] is 1 change it to 2 and decrement freshCount by 1
                            grid[nr][nc] = 2
                            freshCount -= 1
                            q.append((nr,nc))   #Append nr, nc into the q
                        
        if freshCount == 0: #If the freshCount is 0 then return time
            return time
        else:   #Else return -1
            return -1