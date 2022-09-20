intervals = [[1,2],[3,5],[6,7],[10,11],[12,16]]
newInterval = [4,8]
def insert(intervals, newInterval):
    if not intervals:
        if newInterval:
            return [newInterval]
        else:
            return [[]]
    low = newInterval[0]
    high = newInterval[1]
    low_not_found = True
    high_not_found = True

    new_list = []
    new_list_count = 0
    
    if low > intervals[len(intervals)-1][1]:
        print(intervals[len(intervals)-1][1], low)
        intervals.append(newInterval)
        return intervals
    

    for i in range(0,len(intervals)):
        if not high_not_found:
            new_list.append(intervals[i])
        
        if low_not_found:
            if low <= intervals[i][0]:
                new_list.append([low,])
                low_not_found = False
            elif low <= intervals[i][1]:
                new_list.append([intervals[i][0],])
                low_not_found = False
            else:
                new_list.append(intervals[i])
                new_list_count += 1
                                     
        if not low_not_found and high_not_found:
            if high < intervals[i][0]:                                   
                new_list[new_list_count].append(high)
                high_not_found = False
                new_list.append(intervals[i])
            elif high >= intervals[i][0] and high <= intervals[i][1]:
                new_list[new_list_count].append(intervals[i][1])
                high_not_found = False
    
    if high > intervals[len(intervals)-1][1]:
        new_list[len(new_list)-1].append(high)

    return new_list

print(insert(intervals,newInterval))
print(insert([[1,5]], [2,7]))
print(insert([[1,5]], [5,7]))
print(insert([[1,5]], [6,8]))