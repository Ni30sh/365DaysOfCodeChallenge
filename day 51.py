def countTriplets(arr, target):
    n = len(arr)
    count = 0
    
    # Iterate through the array, fixing one element at a time
    for i in range(n - 2):
        # Use two pointers to find pairs that sum up to target - arr[i]
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                count += 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return count

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 15
print(countTriplets(arr, target))  # Output: 4