import heapq
min_heap = [9,4,8,3,5,1]
heapq.heapify(min_heap)
print(min_heap)
heapq.heappop(min_heap)
print(min_heap)

max_heap = [9,4,8,3,5,1]

heapq._heapify_max(max_heap)
print(max_heap)
heapq._heappop_max(max_heap)
print(max_heap)