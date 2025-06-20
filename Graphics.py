from PIL import Image, ImageDraw, ImageFont
from Interface import *

def CreateBlankGraphic():
    graphic = Image.new('1', [900,1100], 'white')
    draw = ImageDraw.Draw(graphic)
    
    #Drawing main borders
    draw.line([(100, 1000), (100, 0)], fill='black', width=2)
    draw.line([(100, 1000), (900, 1000)], fill='black', width=2)
    
    #Font and text size
    currentFont = ImageFont.truetype('arial.ttf', size=20)
    
    for i in range(5):
        #Drawing grid
        draw.line([(100, 1200 - ((i + 1) * 200)), (900, 1200 - ((i + 1) * 200))], fill='black', width=1)
        #Drawing text
        currentText = str(-60 + (i * 10))
        draw.text((60, 990 - (200 * i)), currentText, font = currentFont, fill = 'black')
        
    for i in range(4):
        #Drawing grid
        draw.line([(100 + (i + 1) * 200, 1000), (100 + (i + 1) * 200, 0)], fill='black', width=1)
        #Drawing text
        currentText = str(1500 + (i * 25))
        draw.text(((80 + (i * 200)), 1010), currentText, font = currentFont, fill = 'black')
    
    return graphic

def SetPosition(data): #Converts string value to an integer position on a graphic
    XPos = ((float(data[0]) - 1500) * 8) + 100
    YPos = abs(((float(data[1]) + 10) * 20))
    return [int(XPos), int(YPos)]
    
def CreateGraphic(datalist):
    graphic = CreateBlankGraphic()
    draw = ImageDraw.Draw(graphic)
    previtem = datalist[0]
    for item in datalist[1:]:
        draw.line([SetPosition(previtem), SetPosition(item)], fill='black', width=2)
        previtem = item  
    return graphic


#Example call
print("Enter path")    
path = str(input())
datalist = ReadFile(path)
datalist = SliceData(datalist, 1500, 1600)
img = CreateGraphic(datalist) 
XlsxOutput(datalist, "1")
img.save("2.png")