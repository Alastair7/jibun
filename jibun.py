from pathlib import Path
from datetime import date
import calendar

# Creates journey starting point.
base_path = Path(".")
journey_path = Path.joinpath(base_path, Path("journey"))

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
while user_input != "-1" and user_input != "2":
    print("Hey Adventurer! What would you like to do?")
    print("""
          1 - Add my daily log
          2 - Exit
          """)
    user_input = input("I want to... >> ")
    match user_input:
        case "1":
            # Get the current month and search for file, if not exists then create it.
            current_month_name = calendar.month_name[date.today().month]

            month_path = Path.joinpath(journey_path, str(date.today().year), current_month_name + '.txt')
            if not (month_path.exists()):
                print(month_path, "does not exist. Creating the path.")
                Path.touch(month_path)
            # Add the log by comparing dates. If the log exists, update the log
            with month_path.open("w+") as f:
                f.writelines(["Test\n", "Test2\n"])
                print(f.readlines())
            # Log format: Line -> Current Date, Kcal and Protein Limits, Kcal and Protein
            # Last Line -> Totals
