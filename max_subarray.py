from tkinter import N


arr = [-1, 4, 2, -1, 3, 5]

current_max = 0
global_max = arr[0]
for number in arr:
    current_max = number + current_max
    if current_max < number:
        current_max = number
    if global_max < current_max:
        global_max = current_max

print(global_max)