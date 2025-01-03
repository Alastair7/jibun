from pathlib import Path
from datetime import date

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