from pathlib import Path
from datetime import date
import calendar
import journal_helper

journal_helper.init_journey()

current_month = date.today().month
month_name = calendar.month_name[current_month]

base_path = Path(".")
journey_path = Path.joinpath(base_path, Path("journey"))
month_file = Path.joinpath(journey_path, str(date.today().year), month_name + ".txt")

menu_options = """
          1 - Add my daily log
          2 - Set my energy limit
          3 - Exit
          """


energy_limit = ""
adventurer_input = ""

while adventurer_input != "-1" and adventurer_input != "3":
    print("Hey Adventurer! What would you like to do?")
    print(menu_options)
    adventurer_input = input("I want to: ")
    match adventurer_input:
        case "1":
            calories = input('Kcal >> ')
            protein = input('Protein >> ')
            journal_helper.add_daily_log(month_file, calories, protein, energy_limit)
        case "2":
            energy_limit = journal_helper.set_adventurer_limits()