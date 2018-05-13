from PIL import Image
import binascii

i = 0
photo = Image.open("test.png")
imgPixelAccess = photo.load()
imgSize, imgMode = photo.size, photo.mode
print(imgSize, imgMode)
binaire = ""
while i < photo.size[1]:
    if imgPixelAccess[i,0][i%3]%2 == 1:
        binaire = binaire + "0"
    else:
        binaire = binaire + "1"
    i=i+1
oui = open("oui.txt","w")
oui.write(binaire)