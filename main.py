from Interface import *

while True:
    print('Enter the path to .csv file. Type "Q" to quit')

    path = ("C:\\Users\\Admin\\Desktop\\Папка с папками\\Практика\\Practice\\3.csv")
    #path = str(input())
    IsQuitting = False
    if path == "Q":
        print("Quitting...")
        break
    while not(os.path.exists(path)):
        print("Path does not exist")
        path = str(input())
        if path == "Q":
            print("Quitting...")
            IsQuitting = True
            break
    if IsQuitting:
        break

    datalist = ReadFile(path)

    #Добавить защиту от слабоумных
    print("Enter the path to save .xlsx file")
    xlsxpath = ("C:\\Users\\Admin\\Desktop\\Tests\\Test.xlsx")
    #xlsxpath = str(input())
    print("Where to save graphic file?")
    imgpath = ("C:\\Users\\Admin\\Desktop\\Tests\\3.png")
    #imgpath = str(input())

    print("Analysing...")
    AnalyseData(datalist, xlsxpath, imgpath)
    print("Done")
    break #Не забыть убрать