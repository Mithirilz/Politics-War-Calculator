def main():
    calc_turns_for_goal_treasury(desired_treasury=1000, current_treasury=50, net_income=200) 
    return

def calc_turns_for_goal_treasury(desired_treasury: int, current_treasury: int, net_income: int):
    print(f"Desired treasury: {desired_treasury}")
    print(f"Current treasury: {current_treasury}")
    print(f"Net income: {net_income}")

    profit_needed = desired_treasury - current_treasury

    if (profit_needed) > 0 or (desired_treasury < current_treasury):

        print(f"Financial gap between the treasuries {desired_treasury - current_treasury}")

    else:
        print(f"Why do you want to lose money??")
        return  
    
    turns_needed = (profit_needed / net_income)

    print(f"The amount of turns needed to reach desired treasury: {turns_needed}")
    print(f"Time taken to reach desired treasury: {turns_needed*2}")

    return

main()