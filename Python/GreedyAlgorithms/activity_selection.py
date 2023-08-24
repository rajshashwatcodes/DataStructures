def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort activities by end times
    selected_activities = [activities[0]]
    
    for activity in activities[1:]:
        if activity[0] >= selected_activities[-1][1]:
            selected_activities.append(activity)
    
    return selected_activities

# Example usage
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
selected = activity_selection(activities)
print("Selected activities:")
for activity in selected:
    print(activity)
