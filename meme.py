from PIL import ImageDraw, ImageFont

class Meme_Maker:
    def __init__(self, font, minSize=8, maxSize=72):
        self.fontList = [ImageFont.truetype(font, fontSize) for fontSize in range(minSize, maxSize+1)]

    def makeMeme(self, img, wordsTop=None, wordsBot=None, col=(255, 255, 255, 255)):
        draw = ImageDraw.Draw(img)
        limWords = wordsTop if len(wordsTop) > len(wordsBot) else wordsBot
        
        i = 0
        try:
            while(self.fontList[i].getsize(limWords)[0] < int(img.width*7/8)):
                i+=1
        except IndexError:
            i = len(self.fontList)
            
        font = self.fontList[i-1]
        
        xyTop = (int((img.width - font.getsize(wordsTop)[0])/2), int(img.height/32))
        xyBot = (int((img.width - font.getsize(wordsBot)[0])/2), int(img.height*31/32 - font.getsize(wordsBot)[1]))
    
        draw.text(xyTop, wordsTop, col, font=font)
        draw.text(xyBot, wordsBot, col, font=font)
