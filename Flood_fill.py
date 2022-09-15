#input
image = [[1,1,1],[1,1,0],[1,0,1]]
'''
[1,1,1]
[1,1,0]
[1,0,1]
'''
sr = 1
sc = 1
color = 2

#algorithim

image_row_length = len(image)
image_column_length = len(image[0])

queue = []
visited = []
root_color = image[sr][sc]

queue.append((sr,sc))

while queue:
    point = queue.pop(0)
    visited.append(point)
    row = point[0]
    column = point[1]

    if image[row][column] == root_color:
        image[row][column] = color
    
    if row+1 < image_row_length:
        if (row+1,column) not in visited:
            if image[row+1][column] == root_color:
                queue.append((row+1,column))
    
    if column+1 < image_column_length:
        if (row,column+1) not in visited:
            if image[row][column+1] == root_color:
                queue.append((row,column+1))

    if row-1 >= 0:
        if (row-1,column) not in visited:
            if image[row-1][column] == root_color:
                queue.append((row-1,column))
        
    if column-1 >= 0:
        if (row,column-1) not in visited:
            if image[row][column-1] == root_color:
                queue.append((row,column-1))

print(image)