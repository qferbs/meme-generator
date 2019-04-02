from meme import Meme_Maker
from PIL import Image
from pathlib import Path
import random
random.seed()

##open image & wordlist
meme = Meme_Maker("ariblk.ttf")
wordFile = open("words.txt", "r")
wordList = wordFile.read()
wordList = wordList.upper().split()

##get list of all images
path = Path("./Images")
images = ["Images/"+p.name for p in path.iterdir()]

##constants
num = 1000
minW = 200
minH = 200

for i in range(0, num):
    imgUrl = random.choice(images)
    while(1):
        try:
            image = Image.open(imgUrl)
            break
        except:
            print("can't open", imgUrl)
    
    while(image.width < minW or image.height < minH):
        image.close()
        images.remove(imgUrl)
        imgUrl = random.choice(images)
        image = Image.open(imgUrl)
        if(images == []):
            raise Exception("/Images has no valid images!")
    
    top = " ".join([random.choice(wordList) for i in range(0, random.randint(1, 2))])
    bottom = " ".join(random.choice(wordList) for i in range(0, random.randint(1, 2)))

    image = image.convert("RGBA")
    meme.makeMeme(image, top, bottom)

    image.save("Memes/meme%s.png" % i)
