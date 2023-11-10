def coin_change(coins, amount):
    # Initialize an array to store minimum number of coins needed for each amount
    dp = [float('inf')] * (amount + 1)
    
    # Base case: Zero coins needed for zero amount
    dp[0] = 0
    
    # Calculate minimum coins for each amount from 1 to the target amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still infinity, no combination of coins is possible
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
result = coin_change(coins, amount)
print(f"Minimum number of coins needed for amount {amount}: {result}")
