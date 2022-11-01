"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj = {}    #Adjacency matrix
        totalImportance = 0 #Initialize totalImportance as 0
        q = deque() #Initialize q using deque
        q.append(id)    #Append the id into the q
        for emp in employees:   #For every employees
            adj[emp.id] = [emp.importance, emp.subordinates]    #Insert the importance and all the subordinates for the employee id 
            
        while q:    #Cntinue till the q is empty
            currEmployee = q.popleft()  #Pop the first element in the q using popleft and store it in currEmployee
            totalImportance+= adj[currEmployee][0]  #Add totalImportance with importance of the employee in the adjacency matrix
            
            for subordinate in adj[currEmployee][1]:    #For every subordinate in teh adjacency matrix
                q.append(subordinate)   #Append the subordinate into the q
                
        return totalImportance  #Return totalImportance
        