def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Initialize an array to store the length of the LIS ending at each index

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage
sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = longest_increasing_subsequence(sequence)
print(f"The length of the longest increasing subsequence is: {result}")
