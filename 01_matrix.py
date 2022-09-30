def updateMatrix(matrix):
    distance = dict()
    #first pass if not 0 set to infinity
    '''
    1 1 1     
    1 1 1
    1 1 0
    
    0 1 1
    1 1 1
    1 1 1
    
    1 1 1
    1 0 1
    1 1 1
    
    c c c
    c 0 1
    c 1 2
    
    2 1 2
    1 0 1
    2 1 2    
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                if i-1 >= 0 and j-1 >= 0:
                    if matrix[i-1][j] < float('inf') or matrix[i][j-1] < float('inf'):
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + 1
                    else:
                        matrix[i][j] = float('inf')
                    
                elif i-1 >= 0:
                    if matrix[i-1][j] < float('inf'):
                        matrix[i][j] = matrix[i-1][j] + 1
                    else:
                        matrix[i][j] = float('inf')

                elif j-1 >= 0:
                    if matrix[i][j-1] < float('inf'):
                        matrix[i][j] = matrix[i][j-1] + 1
                    else:
                        matrix[i][j] = float('inf')
                        
                else:
                    matrix[i][j] = float('inf')
    
    row_len = len(matrix)
    column_len = len(matrix[0])

    for i in reversed(range(len(matrix))):
        for j in reversed(range(len(matrix[0]))):
        
            if matrix[i][j] != 0:
                
                if i+1 < row_len and j+1 < column_len:
                    matrix[i][j] = min(matrix[i+1][j]+1, matrix[i][j+1]+1, matrix[i][j])

                elif i+1 < row_len:
                    matrix[i][j] = min(matrix[i+1][j]+1, matrix[i][j])

                elif j+1 < column_len:
                    matrix[i][j] = min(matrix[i][j+1]+1, matrix[i][j])

    return matrix
    

                

                        
            
                        
    
print(updateMatrix([[1,1,1],[1,1,1],[1,1,0]]))
print(updateMatrix([[0,1,1],[1,1,1],[1,1,1]]))
print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(updateMatrix([[1,1,1],[1,0,1],[1,1,1]]))