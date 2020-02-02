import os
import random
import math
from PIL import Image

fishBody = []
fishTail = []
fishEye = []
fishFin = []

W = 1920
H = 1080

NumOfFish = 100

def test():
    testIm = Image.open('fishFin1.png')
    testIm = randomPicture(testIm)
    testIm = testIm.resize((1000,2000))
    testIm.save('type1/tiled.png')

def main():
    initial()
    for i in range(NumOfFish):
        name = "fish_" + str(i+1) + ".png"
        temp = Image.new('RGBA', (W,H), (0, 0, 0, 0))
        sample = getPicture() #[body,tail,eye,fin]
        temp = paste(temp, sample)
        temp.save("type1/" + name)

def getPicture():
        result = []
        randNum = random.randint(0,len(fishBody) - 1)
        result.append(randomPicture(fishBody[randNum].copy()))
        randNum = random.randint(0,len(fishTail) - 1)
        result.append(randomPicture(fishTail[randNum].copy()))

        #randNum = random.randint(0,len(fishEye) - 1)
        #result.append(randomPicture(fishEye[randNum].copy()))

        randNum = random.randint(0,len(fishFin) - 1)
        result.append(fishFin[randNum].copy())
        return result

def paste(temp, sample):
        maxW = 0
        maxH = 0
        bodyWidth,bodyHeight = sample[0].size


        tailWidth, tailHeight = sample[1].size
        temp.paste(sample[1], (bodyWidth - math.floor(0.3*tailHeight),math.floor((H-tailHeight)/2 - 5)), mask = sample[1])
        temp.paste(sample[0], (0,math.floor((H-bodyHeight)/2)), mask = sample[0])

        finWidth, finHeight = sample[2].size
        temp.paste(sample[2], (math.floor(3*bodyWidth/7),math.floor((H-finHeight)/2)), mask = sample[2])

        maxW = tailWidth + bodyWidth
        maxH = max(tailHeight,bodyHeight)
        temp = temp.crop((0 ,
                            math.floor((H-maxH)/2) - 100,
                            maxW,
                            math.floor(H - (H-maxH)/2) + 100))
        #temp.paste(sample[3], (H/2,bodyWidth/7), mask = sample[3])
        temp.resize((1920,1080))
        return temp

def randomPicture(picture):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(5, 15) / 10.0
        height, width = picture.size
        for i in range(height):
            for j in range(width):
                RGB = picture.getpixel( (i,j) )
                if (RGB[0] > 10 and RGB[1] > 10 and RGB[2] > 10) or RGB[3] > 0.1:
                    picture.putpixel((i,j),((RGB[0] + r)%255, (RGB[1] + g)%255, (RGB[2] + b)%255))
        picture = picture.resize((math.floor(c * height), math.floor(c * width)))
        return picture

def initial():
    fileType = ["fishBody","fishFin","fishTail","fishEye"]
    allFile = readFile();
    for i in allFile:
        if fileType[0] in i:
            fishBody.append(Image.open(i))
        elif fileType[1] in i:
            fishFin.append(Image.open(i))
        elif fileType[2] in i:
            fishTail.append(Image.open(i))
        elif fileType[3] in i:
            fishEye.append(Image.open(i))
def readFile():
    fileType = [".jpg",".jpeg",".png"]
    temp = os.listdir('.')
    allFile = [];
    for i in temp:
        for j in fileType:
            if j in i:
                allFile.append(i)
    return allFile
main()
