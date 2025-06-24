from PIL import Image, ImageDraw, ImageFont
from Data_processing import *

def CreateBlankGraphic():
    graphic = Image.new('1', [1000,1100], 'white')
    draw = ImageDraw.Draw(graphic)
    
    #Drawing main borders
    draw.line([(100, 1000), (100, 0)], fill='black', width=4)
    draw.line([(100, 1000), (900, 1000)], fill='black', width=4)
    draw.line([(900, 1000), (900, 0)], fill='black', width=4)
    
    #Set font and text size
    currentFont = ImageFont.truetype('arial.ttf', size=32)

    #Sign axis (Unnecessary)
    #currentText = "Длина волны, нм"
    #draw.text((350, 1050), currentText, font = currentFont, fill = 'black')
    
    #currentText = "Оптический сигнал, дБм"
    #fontimage = Image.new('1', [380, 40], 'black')
    #ImageDraw.Draw(fontimage).text((0, 0), currentText, font = currentFont, fill = 'white')
    #fontimage = fontimage.rotate(90, expand=True)
    #graphic.paste('black', box=(20, 350), mask=fontimage)

    #Change font and text size
    currentFont = ImageFont.truetype('arial.ttf', size=20)
    
    for i in range(5):
        #Drawing grid
        draw.line([(100, 1200 - ((i + 1) * 200)), (900, 1200 - ((i + 1) * 200))], fill='black', width=2)
        #Drawing text
        currentText = str(-60 + (i * 10))
        draw.text((60, 990 - (200 * i)), currentText, font = currentFont, fill = 'black')
        
    for i in range(4):
        #Drawing grid
        draw.line([(100 + (i + 1) * 200, 1000), (100 + (i + 1) * 200, 0)], fill='black', width=2)
        #Drawing text
        currentText = str(1500 + (i * 25))
        draw.text(((80 + (i * 200)), 1010), currentText, font = currentFont, fill = 'black')
    currentText = str(1600)
    draw.text((880, 1010), currentText, font = currentFont, fill = 'black')
    #Drawing secondary grid
    for i in range(25):
        draw.line([(100, 1000 - ((i + 1) * 40)), (900, 1000 - ((i + 1) * 40))], fill='black', width=1)
    for i in range(20):
        draw.line([(100 + (i + 1) * 40, 1000), (100 + (i + 1) * 40, 0)], fill='black', width=1)
    
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