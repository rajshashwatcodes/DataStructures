def matrix_chain_multiplication(dims):
    n = len(dims) - 1

    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')  
            
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]


matrix_dimensions = [10, 30, 5, 60]
minimum_cost = matrix_chain_multiplication(matrix_dimensions)
print(f"Minimum number of multiplications needed: {minimum_cost}")
