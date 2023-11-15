def subset_sum_recursive(nums, target, current=[]):
    if target == 0:
        # Found a subset that sums up to the target
        print(current)
        return

    if not nums:
        # Reached the end of the list
        return

    # Include the current number in the subset
    subset_sum_recursive(nums[1:], target - nums[0], current + [nums[0]])

    # Exclude the current number from the subset
    subset_sum_recursive(nums[1:], target, current)

# Example usage
numbers = [2, 4, 6, 8]
target_sum = 10

print(f"All subsets with sum {target_sum}:")
subset_sum_recursive(numbers, target_sum)
