from datetime import date, datetime
from pathlib import Path

from Interface import *

# Work mode selection
def handler_startup():
    mode = -1
    while mode !=  0:
        mode = -1

        # Awaiting of correct user input
        while mode != '1' and mode != '2' and mode != '0':
            print('1. Multiple records\n'
                  '2. Single record\n'
                  '0. Stop program\n'
                  'Choose working mode: ')
            mode = input()

        # Redirection to working modes
        match mode:
            case '1': handler_multiply_files()
            case '2': handler_single_file()
            case '0': break

# Work with multiply files
def handler_multiply_files():
    # Validation of directory requirements
    if not check_directory_requirements():
        if not handler_no_directory():
            return

    print('Xls file and graphs folder with current datetime will be created.')

    # Getting list of .csv files in record directory
    files = get_file_names('records', '.csv')

    # Current date and time
    date = str(datetime.now())
    date = date.replace(':', '.')

    # Creation of result directory with current datetime in name
    resultdir = 'results/' + date
    os.makedirs(resultdir, exist_ok=True)

    imgdir = resultdir + '/graphs'
    os.makedirs(imgdir, exist_ok=True)

    imgdir = imgdir + '/'

    # Path for .xlsx file
    xlsxpath = resultdir + '/result.xlsx'

    print("Analysing...")

    # Data analysis for every .csv file in records directory
    for path in files:
        dataset = ReadFile('records/' + path)
        record_name = os.path.splitext(path)[0]
        imgpath = str(Path(imgdir + record_name + '.png').resolve())
        AnalyseData(dataset, xlsxpath, imgpath, record_name)

    print("Done")

# Conflict resolution when directory requirements are not met
def handler_no_directory():
    print('For correct work of program records and results folder required.\n'
          'Create folders? (y/n): ')

    userinput = ''

    while userinput != 'y' and userinput != 'n':
        print('Incorrect input. Create folders? (y/n):  ')
        userinput = input()

    if userinput == 'y':
            prepare_folders()
            return True

    return False


def handler_single_file():
    print('Enter absolute path to .csv file. Type "Q" to quit')

    path = str(input())
    IsQuitting = False
    if path == "Q":
        print("Quitting...")
        return
    while not(os.path.exists(path)):
        print("Path does not exist")
        path = str(input())
        if path == "Q":
            print("Quitting...")
            IsQuitting = True
            return
    if IsQuitting:
        return

    datalist = ReadFile(path)

    #Добавить защиту от слабоумных
    #print("Enter the path to save .xlsx file")
    #xlsxpath = str(input())
    #print("Where to save graphic file?")
    #imgpath = str(input())

    #Sets the date of today, but not the time, because single files can't be loaded simultaneously 
    todayDate = str(date.today())
    todayDate = todayDate.replace(':', '.')

    xlsxpath = 'results/' + todayDate + '-singles.xlsx'
    imgdir = 'results/graphs/' + todayDate + '-singles'
    os.makedirs(imgdir, exist_ok=True)
    imgdir = imgdir + '/'
    record_name = os.path.splitext(os.path.splitext(os.path.basename(path))[0])[0]

    print("Analysing...")
    AnalyseData(datalist, xlsxpath, imgdir + record_name + '.png', record_name)
    print("Done")
    return

