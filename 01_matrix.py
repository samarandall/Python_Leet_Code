def updateMatrix(matrix):
    map = {}
    row_length = len(matrix)
    column_length = len(matrix[0])
    for i in range(0,row_length):
        for j in range(0,column_length):
            if matrix[i][j] == 0:
                map[(i,j)] = 0
            else: #need to implement check if all 4 surrounding nodes are not 0, then curr node = None
                if i-1 >= 0:
                    map[i,j] = matrix[i-1][j]+1
                if j-1 >= 0:
                    if not map.get(i,j) or map.get(i,j) > matrix[i][j-1]:
                        map[i,j] = matrix[i][j-1]+1
                    
                if i+1 < row_length:
                    if not map.get(i,j) or map.get(i,j) > matrix[i+1][j]:
                        map[i,j] = matrix[i+1][j]+1
                        
                if j+1 < row_length:
                    if not map.get(i,j) or map.get(i,j) > matrix[i][j+1]:
                        map[i,j] = matrix[i][j+1]+1
    queue = []
    queue.append(row_length,column_length)

    while queue:
        point = queue.pop()
        if point[0]-1 >= 0:
            queue.append(point[0]-1, point[1])
        if point[1]-1 >= 0:
            queue.append(point[0],point[1]-1)
        
        
            
                        
    
    
print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))