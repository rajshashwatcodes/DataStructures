def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    value_per_weight = [(item[0] / item[1], item[0], item[1]) for item in items]
    
    # Sort the items based on the value-to-weight ratio in descending order
    value_per_weight.sort(reverse=True)
    
    total_value = 0
    selected_items = []
    
    for ratio, value, weight in value_per_weight:
        # If the entire item can be included, add its value to the total and update the remaining capacity
        if capacity >= weight:
            total_value += value
            capacity -= weight
            selected_items.append((value, weight))
        else:
            # Otherwise, include a fraction of the item to fill the remaining capacity
            fraction = capacity / weight
            total_value += fraction * value
            selected_items.append((fraction * value, fraction * weight))
            break  # Knapsack is full, so exit the loop
    
    return total_value, selected_items


my_items = [(60, 10), (100, 20), (120, 30)]
knapsack_capacity = 50

max_value, selected_items = fractional_knapsack(my_items, knapsack_capacity)

print("Maximum value:", max_value)
print("Selected items:", selected_items)
