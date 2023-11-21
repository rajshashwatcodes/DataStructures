def max_subarray_sum(arr):
    if not arr:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print(f"The maximum subarray sum is: {result}")
