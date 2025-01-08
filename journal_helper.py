import calendar
from datetime import date
from pathlib import Path

def init_journey():
    journey_path = Path("./journey")
    if not Path.exists(journey_path):
        print("Your journey has not started yet...")
        print("Starting a new journey in: ", journey_path.absolute())
        Path.mkdir(journey_path)

        current_year = str(date.today().year)
        year_path = Path.joinpath(journey_path, current_year)
        Path.mkdir(year_path, parents=True, exist_ok=True)

        current_month = date.today().month
        month_name = calendar.month_name[current_month]
        month_file = Path.joinpath(year_path, month_name + ".txt")
        Path.touch(month_file, exist_ok=True)

def set_adventurer_limits():
    kcal = input('Kcal Limit: ')
    protein = input('Protein Limit: ')

    return ",".join([kcal, protein]) 

def add_daily_log(month_file, kcalories, protein, energy_limit):
    if len(energy_limit) == 0:
        print("Seems that you don't have any energy limit set, embrace your limits.")
        energy_limit = set_adventurer_limits()

    log_data = ",".join([kcalories, protein])
    cur_date = date.today().isoformat()

    base_log = cur_date + " " + energy_limit + " " + log_data + "\n"

    with open(month_file) as file:
        file_lines = file.readlines()
    
    for line in file_lines:
        if cur_date in line:
            line_index = file_lines.index(line)
            file_lines[line_index] = base_log
            break
    else:
        file_lines.append(base_log)

    with open(month_file, "w+") as f:
        f.writelines(file_lines)