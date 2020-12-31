def find_empty(puzzle):
    #returns empty position 
    for r in range(9):
        for c in range(9):

         if puzzle[r][c] == -1:
            return r,c
    return None,None

#check if value exist already
def check(puzzle,num,row,col):
    #check row
    row_exist=puzzle[row]
    if num in row_exist:
        return False
    #check column
    col_exist=[]
    for i in range(9):
        col_exist.append(puzzle[i][col])
        if num in col_exist:
            return False
    
    #check subgroup 

    row_beg=(row//3)*3
    col_beg=(col//3)*3

    for r in range(row_beg,row_beg+3):
        for c in range(col_beg,col_beg+3):
            if puzzle[r][c]==num:
                return False


    return True       

     

        
        
        
def sudoku(puzzle):
   
    
    row,col= find_empty(puzzle)     
    
    if row is None:
        return True

    for num in range (1,10):
        if check(puzzle,num,row,col):
            puzzle[row][col]= num

    if sudoku(puzzle):
         return True

if __name__ == '__main__':
    puzzle = [
        [-1,2,7,1,5,4,3,9,6],
      [9,6,5,3,-1,7,1,4,8],
      [3,4,1,6,8,9,7,5,2],
      [5,9,3,-1,6,8,2,7,1],
      [4,7,2,5,1,3,6,8,-1],
      [6,1,-1,9,7,2,4,3,5],
      [7,8,6,2,3,5,-1,1,4],
      [1,5,4,7,9,6,8,-1,3],
      [2,-1,9,8,4,1,5,6,7] 
    ]
    print(sudoku(puzzle))
    print(puzzle)



    