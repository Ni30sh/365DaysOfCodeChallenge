def mergeSort(arr, n):
    # Create temp array
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)

def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0
    
    if left < right:
        # Find mid point
        mid = (left + right)//2

        # Divide into two parts
        inv_count += _mergeSort(arr, temp_arr, left, mid)
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)

        # Merge two parts
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

def merge(arr, temp_arr, left, mid, right):
    i = left      # Starting index of left subarray
    j = mid + 1   # Starting index of right subarray
    k = left      # Starting index of temporary array
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1

    # Copy remaining elements
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy back to original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        
    return inv_count

def getInversions(arr, n):
    return mergeSort(arr, n)

# Example usage:
if __name__ == '__main__':
    arr = [2, 4, 1, 3, 5]
    n = len(arr)
    print(getInversions(arr, n))  # Output: 3