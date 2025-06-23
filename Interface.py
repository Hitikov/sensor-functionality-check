import os
import csv
import xlsxwriter
from openpyxl import load_workbook, cell
from Data_processing import *
from Function_characteristics import *

def ReadFile(path):
    with open(path, newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        return ReaderToList(filereader)
           
def ReaderToList(filereader):
    datalist = []
    for row in filereader:
        datalist.append(tuple(row))
    datalist = SliceData(datalist, 1500, 1600)
    datalist = convert_to_float(datalist)
    return datalist

def XlsxOutput(datalist, filename):
    name = filename
    workbook = xlsxwriter.Workbook(name + '.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    for item1, item2 in (datalist):
        worksheet.write(row, col, float(item1))
        worksheet.write(row, col + 1, float(item2))
        row += 1
    workbook.close()

def AnalyseData(datalist, path): 
    #Intial create
    if not(os.path.exists(path)):   
        workbook = xlsxwriter.Workbook(path)
        worksheet = workbook.add_worksheet()

        #Field labels
        worksheet.write(0, 0, "Номер с примечанием")
        worksheet.write(0, 1, "Потери, дБ")
        worksheet.write(0, 2, "Контраст интерференции, дБ")
        worksheet.write(0, 3, "FSR")
        worksheet.write(0, 4, "Спектр")
        worksheet.write(0, 5, "Состояние")

        workbook.close()

    #Find first free row
    workbookLoader = load_workbook(filename = path)
    sheet = workbookLoader.active
    freeRow = sheet.max_row + 1

    number = "0"
    losses, contrast, FSR = dataset_analysis(datalist)
    spectre_link = "0"
    condition = "0"

    data = [number, losses, contrast, FSR, spectre_link, condition]
    for i in range(5):
        cell = sheet.cell(freeRow, i + 1).value = data[i]

    workbookLoader.save(path)
    return 0      


#Example call
print("Enter path")    
path = str(input())
datalist = ReadFile(path)
datalist = SliceData(datalist, 1500, 1600)
#img = CreateGraphic(datalist) 
XlsxOutput(datalist, "1")
#img.save("2.png")
AnalyseData(datalist, "C:\\Users\\Admin\\Desktop\\Tests\\Test.xlsx")