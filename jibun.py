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

def add_log(calories, protein):
    current_month_name = calendar.month_name[date.today().month]
    month_path = Path.joinpath(journey_path, str(date.today().year), current_month_name + '.txt')

    if not month_path.exists():
        print(month_path, "does not exist. Creating the path.")
        Path.touch(month_path)


    # Get Current day log line
    log_data = ','.join([calories, protein])
    cur_date = date.today().isoformat()

    log_line = cur_date + " " + log_data

    with open(month_path) as f:
        file_lines = f.readlines()

    for line in file_lines:
        if cur_date in line:
            line_index = file_lines.index(line)
            file_lines[line_index] = log_line
            break
        else:
            file_lines.append(log_line + "\n")
            break
    else:
        file_lines.append(log_line + "\n")

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