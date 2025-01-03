from pathlib import Path
from datetime import date

basePath = Path(".")
journeyPath = Path.joinpath(basePath, Path("journey"))

if not Path.exists(journeyPath):
    print("Journey not found.")
    print("Starting a new journey in path:", journeyPath.absolute())
    Path.mkdir(journeyPath)
    
    for item in journeyPath.iterdir():
        item.exists() and item.is_dir()
        
    print('Creating your starting year directory as well:', date.today().year)
    startingYearPath = Path.joinpath(journeyPath, str(date.today().year))
    Path.mkdir(startingYearPath)