from math import ceil

def main():
    calc_turns_for_goal_treasury(desired_treasury=2000000, current_treasury=1327257.58, net_income=109257.41) 
    return

def calc_turns_for_goal_treasury(desired_treasury: int, current_treasury: int, net_income: int):
    print(f"Desired treasury: RM{desired_treasury:,}")
    print(f"Current treasury: RM{current_treasury:,}")
    print(f"Net income: RM{net_income:,}")

    profit_needed = desired_treasury - current_treasury

    if (profit_needed) > 0 or (desired_treasury < current_treasury):
        rounded_number = round(profit_needed, 2) 
        print(f"Financial gap between the treasuries: RM{rounded_number:,}")

    else:
        print(f"Why do you want to lose money??")
        return  
    
    turns_needed = ceil((profit_needed / net_income))

    print(f"The amount of turns needed to reach desired treasury: {int(turns_needed)}")
    print(f"Time taken to reach desired treasury: {int(turns_needed*2)} hours")

    return

main()