def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    
    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])
    
    non_overlap_end = intervals[0][1]
    count = 0
    
    # Check each interval for overlap
    for i in range(1, len(intervals)):
        if intervals[i][0] < non_overlap_end:
            # Overlap found - need to remove this interval
            count += 1
        else:
            # No overlap - update last non-overlapping end time
            non_overlap_end = intervals[i][1]
    
    return count

# Test cases
test_cases = [
    [[1,2], [2,3], [3,4], [1,3]],
    [[1,3], [1,3], [1,3]],
    [[1,2], [5,10], [18,35], [40,45]]
]

for intervals in test_cases:
    print(eraseOverlapIntervals(intervals))