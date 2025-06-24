import os
import csv
import xlsxwriter
from openpyxl import load_workbook
from Data_processing import *
from Function_characteristics import *
from Graphics import *

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

def AnalyseData(datalist, xlsxpath, imgpath):
    #Intial create
    if not(os.path.exists(xlsxpath)):   
        workbook = xlsxwriter.Workbook(xlsxpath)
        worksheet = workbook.add_worksheet()

        #Field labels
        worksheet.write(0, 0, "Номер с примечанием")
        worksheet.write(0, 1, "Потери, дБ")
        worksheet.write(0, 2, "Контраст интерференции, дБ")
        worksheet.write(0, 3, "FSR")
        worksheet.write(0, 4, "Спектр")
        worksheet.write(0, 5, "Состояние")

        workbook.close()
    

    #Creating and saving the graphic
    img = CreateGraphic(datalist)
    img.save(imgpath)

    #Find first free row
    workbookLoader = load_workbook(filename = xlsxpath)
    sheet = workbookLoader.active
    freeRow = sheet.max_row + 1

    number = str(freeRow - 1)
    losses, contrast, FSR = dataset_analysis(datalist)
    spectre_link = imgpath
    if dataset_validation([losses, contrast], -20, 7):
        condition = "Годен"
    else:
        condition = "Негоден"
    data = [number, losses, contrast, FSR, spectre_link, condition]
    for i in range(6):
        cell = sheet.cell(freeRow, i + 1).value = data[i]

    workbookLoader.save(xlsxpath)