from pathlib import Path
from datetime import date
import calendar

# Creates journey starting point.
base_path = Path(".")
journey_path = Path.joinpath(base_path, Path("journey"))
menu_options = """
          1 - Add my daily log
          2 - Set my energy limit
          3 - Exit
          """
energy_limit = ""
current_month_name = calendar.month_name[date.today().month]

def set_energy_limit():
    kcal_limit = input("Kcal limit >> ")
    protein_limit = input("Protein limit >> ")

    energy_limit = ",".join([kcal_limit, protein_limit])

    return energy_limit


def add_log(calories, protein):
    month_path = Path.joinpath(journey_path, str(date.today().year), current_month_name + '.txt')
    if not month_path.exists():
        print(month_path, "does not exist. Creating the path.")
        Path.touch(month_path)

    if len(energy_limit) == 0:
        print("Seems that you don't have any energy limit set, embrace your limits.")
        energy_limit = set_energy_limit()

    log_data = ','.join([calories, protein])
    cur_date = date.today().isoformat()

    base_log = cur_date + " " +  energy_limit + " " + log_data

    with open(month_path) as f:
        file_lines = f.readlines()

    for line in file_lines:
        if cur_date in line:
            line_index = file_lines.index(line)
            file_lines[line_index] = base_log
            break
        else:
            file_lines.append(base_log + "\n")
            break
    else:
        file_lines.append(base_log + "\n")

    with open(month_path, "w+") as f:
        f.writelines(file_lines)
if not Path.exists(journey_path):
    print("Journey not found.")
    print("Starting a new journey in path:", journey_path.absolute())
    Path.mkdir(journey_path)
    
    for item in journey_path.iterdir():
        item.exists() and item.is_dir()
        
    print('Creating your starting year directory as well:', date.today().year)
    starting_year_path = Path.joinpath(journey_path, str(date.today().year))
    Path.mkdir(starting_year_path)

user_input = ""

while user_input != "-1" and user_input != "3":
    print("Hey Adventurer! What would you like to do?")
    print(menu_options)
    user_input = input("I want to: ")
    match user_input:
        case "1":
            calories = input('Kcal >> ')
            protein_input = input('Protein >> ')
            add_log(calories, protein_input)
        case "2":
            energy_limit = set_energy_limit()