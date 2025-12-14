import random

# ==========================================
# CONFIGURATION (Change these settings!)
# ==========================================
# How many sides does each die have? (Standard is 6)
DIE_SIDES = 6

# The lowest possible sum (1+1=2)
MIN_SUM = 2

# The highest possible sum (6+6=12)
MAX_SUM = DIE_SIDES * 2
# ==========================================


def get_user_input():
    """
    Asks the user how many times to roll.
    Keeps asking until they give a valid number.
    """
    while True:
        print("\n--- Dice Roller Setup ---")
        user_text = input("How many times should we roll the dice? ")
        
        try:
            # Convert the text "100" into the number 100
            number_of_rolls = int(user_text)
            
            if number_of_rolls > 0:
                return number_of_rolls
            else:
                print("Please enter a number greater than 0.")
                
        except ValueError:
            # This runs if they type "banana" instead of a number
            print("Error: That does not look like a whole number.")


def roll_two_dice():
    """
    Simulates rolling two dice.
    Returns the sum (e.g., 3 + 4 = 7).
    """
    # random.randint(a, b) includes both a and b
    die1 = random.randint(1, DIE_SIDES)
    die2 = random.randint(1, DIE_SIDES)
    return die1 + die2


def run_simulation(total_rolls):
    """
    Runs the rolling logic N times.
    Returns a dictionary of the results.
    """
    # 1. Create the scoreboard (Dictionary)
    # We prepare a spot for every possible number (2 through 12)
    # This ensures our data is clean, even if a number is never rolled.
    scoreboard = {}
    
    # Range is (start, stop), so we need MAX_SUM + 1 to include the last number
    for number in range(MIN_SUM, MAX_SUM + 1):
        scoreboard[number] = 0
        
    print(f"\nRolling the dice {total_rolls} times...")

    # 2. Start rolling!
    for i in range(total_rolls):
        result = roll_two_dice()
        
        # Add 1 to the tally for that number
        scoreboard[result] = scoreboard[result] + 1
        
    return scoreboard


def print_results(scoreboard):
    """
    Prints the dictionary in a clean table.
    """
    print("\n" + "="*30)
    print(f"{'SUM':<10} | {'FREQUENCY':<10}")
    print("-" * 30)
    
    # We sort the keys so the table reads 2, 3, 4... instead of random order
    for number in sorted(scoreboard.keys()):
        count = scoreboard[number]
        print(f"{number:<10} | {count:<10}")
        
    print("="*30)


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":    
    # Step 1: Get the number from the user
    rolls = get_user_input()
    # Step 2: Do the math
    final_data = run_simulation(rolls)
    
    # Step 3: Show the chart
    print_results(final_data)