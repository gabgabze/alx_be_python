task = input("Enter your task: ")
priority = input("Choose priority. (high, medium, low): ")
time = input("Is it time-bound? (yes/no): ")

# use match case for priority
# apply if conditions after
match priority:
    case "high":
        if time == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    
    case "low" | "medium":
        if time == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")

    case "_":
        print('Nothing to report')