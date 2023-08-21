def coin_change(coins, amount):
    coins.sort(reverse=True)  # Sort the coins in descending order
    num_coins = 0
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            num_coins += 1
    
    if amount == 0:
        return num_coins
    else:
        return -1  # It's not possible to make the amount with the given coins

# Example usage
coin_denominations = [1, 5, 10, 25]  # Coin denominations in cents
target_amount = 63  # Amount to make using coins

min_coins = coin_change(coin_denominations, target_amount)
if min_coins != -1:
    print(f"Minimum coins needed: {min_coins}")
else:
    print("It's not possible to make the amount with the given coins")
