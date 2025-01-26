def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    
    # Add intervals that come before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    # Add merged interval
    result.append(newInterval)
    
    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
        
    return result

# Test cases
intervals1 = [[1,3], [4,5], [6,7], [8,10]]
newInterval1 = [5,6]
print(insert(intervals1, newInterval1))  # [[1,3], [4,7], [8,10]]

intervals2 = [[1,2], [3,5], [6,7], [8,10], [12,16]]
newInterval2 = [4,9]
print(insert(intervals2, newInterval2))  # [[1,2], [3,10], [12,16]]