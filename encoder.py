from PIL import Image
import binascii,sys
def conversionBinaire(texte):
	binaire = ''.join(map(bin,bytearray(texte,'utf8'))).replace("b","")
	return binaire
i = 0
fileName = input("entrez le nom du fichier")
photo = Image.open(fileName)
imgPixelAccess = photo.load()
imgSize, imgMode = photo.size, photo.mode
print(imgSize, imgMode)
texte = input("entrez le texte a encoder")
texteBinaire = conversionBinaire(texte)
if len(texteBinaire)%3 == 1:
	texteBinaire = texteBinaire + '00'
if len(texteBinaire)%3 == 2:
	texteBinaire = texteBinaire + '0'
print(len(texteBinaire)%3)
print(texteBinaire)
print(imgPixelAccess[0,0][0])

while i < len(texteBinaire):
	if imgPixelAccess[i,0][0] % 2 != int(texteBinaire[i]):
		print("concordance")
	elif imgPixelAccess[i,0][0] == 255:
		imgPixelAccess[i,0]= (int(imgPixelAccess[i,0][0]) - 1,imgPixelAccess[i,0][1],imgPixelAccess[i,0][2])
		print("oui")
	else:
		imgPixelAccess[i,0]= (int(imgPixelAccess[i,0][0]) + 1,imgPixelAccess[i,0][1],imgPixelAccess[i,0][2])
	print(texteBinaire[i])
	i = i + 1
	if imgPixelAccess[i,0][1] % 2 != int(texteBinaire[i]):
		print("concordance")
	elif imgPixelAccess[i,0][1] == 255:
		imgPixelAccess[i,0]= (int(imgPixelAccess[i,0][0]),imgPixelAccess[i,0][1]-1,imgPixelAccess[i,0][2])
		print("oui")
	else:
		imgPixelAccess[i,0]= (int(imgPixelAccess[i,0][0]),imgPixelAccess[i,0][1]+1,imgPixelAccess[i,0][2])
	print(texteBinaire[i])
	i = i + 1
	if imgPixelAccess[i,0][2] % 2 != int(texteBinaire[i]):
		print("concordance")
	elif imgPixelAccess[i,0][2] == 255:
		imgPixelAccess[i,0]= (int(imgPixelAccess[i,0][0]),imgPixelAccess[i,0][1],imgPixelAccess[i,0][2]-1)
		print("oui")
	else:
		imgPixelAccess[i,0]= (int(imgPixelAccess[i,0][0]),imgPixelAccess[i,0][1],imgPixelAccess[i,0][2]+1)
	print(texteBinaire[i])
	i = i + 1
photo.save('C:/Users/spare/Documents/test.png')

