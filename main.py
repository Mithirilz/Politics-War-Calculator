from math import ceil

def main():
    try:
        with open("cache.txt", "r") as cache:
            cache_data = {}

            for lines in cache.readlines():
                index, content = lines.split("=")
                cache_data[index] = content.replace("\n", "")

            is_keep_cache = input("These were the inputs you placed in last session, would you like to keep them?\n" \
                f"Current Treasury: {cache_data["current_treasury"]}\n" \
                f"Desired Treasury: {cache_data["desired_treasury"]}\n" \
                f"Net income: {cache_data["net_income"]}\n\n"
                "y/n\n")
            
            if is_keep_cache.lower() == "y":
                _current_treasury = cache_data["current_treasury"]
                _desired_treasury = cache_data["desired_treasury"]
                _netincome_treasury = cache_data["net_income"]
            
            if is_keep_cache.lower() == "n":
                _current_treasury, _desired_treasury, _netincome_treasury = get_user_inputs()
                store_cache(_current_treasury, _desired_treasury, _netincome_treasury)

    except FileNotFoundError:
        _current_treasury, _desired_treasury, _netincome_treasury = get_user_inputs()
        store_cache(_current_treasury, _desired_treasury, _netincome_treasury)

    _current_treasury = _current_treasury.replace(",", "")
    _desired_treasury = _desired_treasury.replace(",", "")
    _netincome_treasury = _netincome_treasury.replace(",", "")

    calc_turns_for_goal_treasury(desired_treasury=float(_desired_treasury), current_treasury=float(_current_treasury), net_income=float(_netincome_treasury))

    return

def calc_turns_for_goal_treasury(desired_treasury: int, current_treasury: int, net_income: int):
    print(f"\nCurrent treasury: RM{current_treasury:,}")
    print(f"Desired treasury: RM{desired_treasury:,}")
    print(f"Net income: RM{net_income:,}")

    profit_needed = desired_treasury - current_treasury

    if (profit_needed) > 0 or (desired_treasury > current_treasury):
        rounded_number = round(profit_needed, 2) 
        print(f"Financial gap between the treasuries: RM{rounded_number:,}")

    else:
        print(f"Why do you want to lose money??")
        return  
    
    turns_needed = ceil((profit_needed / net_income))
    time_taken = turns_needed*2

    print(f"\nThe amount of turns needed to reach desired treasury: {int(turns_needed)}")
    print(f"Time taken to reach desired treasury: {time_taken} hours")

    if time_taken >= 24:
        print(f"It takes this many days to reach your profit: {round(time_taken/24, 1)} days")

    return

def get_user_inputs():
    _current_treasury = input("What's your current treasury: ")
    _desired_treasury = input("What's the amount of treasury you want to reach: ")
    _netincome_treasury = input("What's your net income: ")

    return _current_treasury, _desired_treasury, _netincome_treasury

def store_cache(_current_treasury, _desired_treasury, _net_income):
    with open("cache.txt", "w") as cache:
        cache.write(f"net_income={_net_income}\n" \
                    f"current_treasury={_current_treasury}\n" \
                    f"desired_treasury={_desired_treasury}")

    return

main()