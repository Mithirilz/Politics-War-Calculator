from math import ceil

def main():
    _desired_treasury = input("What's the amount of treasury you want to reach: ")
    _current_treasury = input("What's your current treasury: ")
    _netincome_treasury = input("What's your net income: ")

    _desired_treasury = _desired_treasury.replace(",", "")
    _current_treasury = _current_treasury.replace(",", "")
    _netincome_treasury = _netincome_treasury.replace(",", "")

    calc_turns_for_goal_treasury(desired_treasury=float(_desired_treasury), current_treasury=float(_current_treasury), net_income=float(_netincome_treasury))

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