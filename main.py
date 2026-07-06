def main():
    calc_turns_for_goal_treasury(desired_treasury=1000, current_treasury=50) 
    return

def calc_turns_for_goal_treasury(desired_treasury: int, current_treasury: int):
    print(f"Desired treasury: {desired_treasury}")
    print(f"Current treasury: {current_treasury}")

    if (desired_treasury - current_treasury) > 0 or (desired_treasury < current_treasury):
        print(f"Financial gap between the treasuries {desired_treasury - current_treasury}")

    else:
        print(f"Why do you want to lose money??")
        return  

    return

main()