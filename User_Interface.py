from datetime import datetime

from Interface import *

def handler_startup():
    mode = -1
    while mode !=  0:
        mode = -1
        while mode != 1 and mode != 2 and mode != 0:
            print('1. Multiply records\n'
                  '2. Single record\n'
                  '0. Stop program\n'
                  'Choose working mode: ')
            mode = int(input())

        match mode:
            case 1: handler_multiply_file()
            case 2: handler_single_file()


def handler_multiply_file():
    if not check_directory_requirements():
        if not handler_no_directory():
            return

    print('Xls file and graphs folder with current datetime will be created.')

    files = get_file_names('records', '.csv')

    date = str(datetime.now())
    date = date.replace(':', '.')

    resultdir = 'results/' + date
    os.makedirs(resultdir, exist_ok=True)

    imgdir = resultdir + '/graphs'
    os.makedirs(imgdir, exist_ok=True)

    xlsxpath = resultdir + '/result.xlsx'
    imgdir = imgdir + '/'

    print("Analysing...")

    for path in files:
        dataset = ReadFile('records/' + path)
        record_name = os.path.splitext(path)[0]
        AnalyseData(dataset, xlsxpath, imgdir + record_name + '.png', record_name)

    print("Done")


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

    path = ("C:\\Users\\Admin\\Desktop\\Папка с папками\\Практика\\Practice\\3.csv")
    #path = str(input())
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
    print("Enter the path to save .xlsx file")
    xlsxpath = ("C:\\Users\\Admin\\Desktop\\Tests\\Test.xlsx")
    #xlsxpath = str(input())
    print("Where to save graphic file?")
    imgpath = ("C:\\Users\\Admin\\Desktop\\Tests\\3.png")
    #imgpath = str(input())

    print("Analysing...")
    AnalyseData(datalist, xlsxpath, imgpath, '3')
    print("Done")
    return

