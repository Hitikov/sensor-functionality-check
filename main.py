from Interface import *

while True:
    print('Enter the path to .csv file. Type "Q" to quit')

    path = str(input())
    if path == "Q":
        print("Quitting...")
        break
    while not(os.path.exists(path)):
        print("Path does not exist")
        path = str(input())

    datalist = ReadFile(path)

    #Добавить защиту от слабоумных
    print("Enter the path to save .xlsx file")
    xlsxpath = str(input())
    print("Where to save graphic file?")
    imgpath = str(input())

    print("Analysing...")
    AnalyseData(datalist, xlsxpath, imgpath)