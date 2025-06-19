import csv
import xlsxwriter

def ReadFile(path):
    with open(path, newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        return ReaderToList(filereader)
           
def ReaderToList(filereader):
    datalist = []
    for row in filereader:
        datalist.append(tuple(row))
    return datalist

def XlsxOutput(datalist):
    print("Enter filename")
    name = str(input())
    workbook = xlsxwriter.Workbook(name + '.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    for item1, item2 in (datalist):
        worksheet.write(row, col, item1)
        worksheet.write(row, col + 1, item2)
        row += 1
    workbook.close()
    
def SliceData(datalist, minvalue, maxvalue):
   return datalist[next((i for i, x in enumerate(datalist[1:]) if float(x[0]) >= minvalue)) + 1:len(datalist) - next((i for i, x in enumerate(datalist[::-1]) if float(x[0]) <= maxvalue))]
    
# Example call
print("Enter path")    
path = str(input())
datalist = ReadFile(path)
datalist = SliceData(datalist, 1500, 1600)
XlsxOutput(datalist)