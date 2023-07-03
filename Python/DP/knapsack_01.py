def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    items = []
    i = n
    j = capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], items

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8
max_value, selected_items = knapsack_01(weights, values, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
