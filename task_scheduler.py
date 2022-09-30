import heapq
def leastInterval(tasks,n):
    task_count = dict()
    for char in tasks:
        if task_count.get(char):
            task_count[char] += 1
        else:
            task_count[char] = 1
        
    heap = list()
    for key in task_count:
        heap.append(task_count[key])
    heapq._heapify_max(heap)
        
    queue = list() #(number of tasks remaining, time back into heap)
    time = 0
    while queue or heap:
        time+=1
        if queue: #push task if task is ready to be put back into heap
            if queue[0][1] == time:
                val = queue[0][0]
                heapq.heappush(heap, val)
                heapq._heapify_max(heap)
                queue.pop(0)

        if heap:
            val = heapq.heappop(heap) - 1
            if val > 0:
                queue.append([val,time+n])
        


    return time

#print(leastInterval(["A","A","A","B","B","B"],2))
print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))
