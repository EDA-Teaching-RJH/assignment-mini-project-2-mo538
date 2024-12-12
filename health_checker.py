#health_checker
def main():
    # Request the user's daily targets and current values for steps and water.
    print("Health App Checker - Track your steps and water intake daily!")# print message the user gets

    try:
        # Get responses for steps and water.
        steps_current, steps_goal = get_values("steps")
        water_current, water_target = get_values("water")
        
        # now calculate percentages
        steps_percentage = calculate_percentage(steps_current, steps_goal)
        water_percentage = calculate_percentage(water_current, water_target)
        
        # this then provides a feedback
        print("Steps: " + health_status(steps_percentage, "Steps"))
        print("Water: " + health_status(water_percentage, "Water"))
        
    except ValueError as e:
        print(f"Error: {e}")


def get_values(category):
    # Allows users to enter current and target values for a category.
    try:
        current = int(input(f"Enter the current {category}: "))
        target = int(input(f"Enter the target {category}: "))
        if current < 0 or target <= 0:
            raise ValueError("Values must be non-negative, and target must be greater than 0.")
        return current, target #
    
    #Arguments include the category name
    
    #Returns a (current, target) as integers.
    except ValueError:
        raise ValueError("Invalid input. Please enter positive integers.")


def calculate_percentage(current, target):
    #Calculates the percentage of current value compared to target.
    return round((current / target) * 100)
    # then returns the percentage as an integer.

def health_status(percentage, category):
    #this provides percentage based on feedback for a specific category.
    if percentage < 50:# Arguments: The percentage of the aim accomplished.
    
    # Returns a string containing feedback based on the percentage.
        return f"You're falling behind on your {category} goal. Keep going you can do this :)!"
    elif percentage < 80:
        return f"You're on track with your {category} goal. Keep it up!"
    elif percentage >= 100:
        return f"Good job! You've exceeded your {category} goal!"
    else:
        return f"You're doing well on your {category} goal. Welldone!"


if __name__ == "__main__":
    main()
