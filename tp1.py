import cv2
import numpy as np
import ctypes
import random
import time
import keyboard

nota_final = 0
user32 = ctypes.windll.user32
winW, winH = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
cars_codificadas = np.array(['hevc/cars_out1.png','hevc/cars_out2.png','hevc/cars_out3.png','hevc/cars_out4.png','jp2/cars_out1.png','jp2/cars_out2.png','jp2/cars_out3.png','jp2/cars_out4.png','vp9/cars_out1.png','vp9/cars_out2.png','vp9/cars_out3.png','vp9/cars_out4.png'])
horses_codificadas = np.array(['hevc/horses_out1.png','hevc/horses_out2.png','hevc/horses_out3.png','hevc/horses_out4.png','jp2/horses_out1.png','jp2/horses_out2.png','jp2/horses_out3.png','jp2/horses_out4.png','vp9/horses_out1.png','vp9/horses_out2.png','vp9/horses_out3.png','vp9/horses_out4.png'])
mountain_codificadas = np.array(['hevc/mountain_out1.png','hevc/mountain_out2.png','hevc/mountain_out3.png','hevc/mountain_out4.png','jp2/mountain_out1.png','jp2/mountain_out2.png','jp2/mountain_out3.png','jp2/mountain_out4.png','vp9/mountain_out1.png','vp9/mountain_out2.png','vp9/mountain_out3.png','vp9/mountain_out4.png'])
barco_codificadas = np.array(['hevc/barco_out1.png','hevc/barco_out2.png','hevc/barco_out3.png','hevc/barco_out4.png','jp2/barco_out1.png','jp2/barco_out2.png','jp2/barco_out3.png','jp2/barco_out4.png','vp9/barco_out1.png','vp9/barco_out2.png','vp9/barco_out3.png','vp9/barco_out4.png'])
lista_apresentavel = []
lista_notas =[]

imagens_mae = ['cars','horses','mountain','barco']
ultima_ordem = ['cars','horses','mountain','barco']

def loadImage(fname,fname1):
	image = cv2.imread(fname)
	center = image.shape
	x = center[1]/2 - winW/2
	y = center[0]/2 - winH/2
	crop_img = image[int(y):int(y+winH), int(x):int(x+winW/2+1)]
	
	image1 = cv2.imread(fname1)
	# I just resized the image to a quarter of its original size
	#image = cv2.resize(image, (0, 0), None, .25, .25)
	center2 = image1.shape
	x2 = center2[1]/2 - winW/2
	y2 = center2[0]/2 - winH/2
	crop_img1 = image1[int(y2):int(y2+winH), int(x2):int(x2+winW/2+1)]
	#grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	# Make the grey scale image have three channels
	#grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)
	numpy_horizontal = np.hstack((crop_img, crop_img1))

	cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)          
	cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

	cv2.imshow('test', numpy_horizontal)

	cv2.waitKey(5000)       

def loadText():
	# Create a black image
	img = np.zeros((winH,winW,3), np.uint8)
	# Write some Text
	img.fill(128)

	font                   = cv2.FONT_HERSHEY_SIMPLEX
	bottomLeftCornerOfText = (int(winW/2.7),int(winH/5))
	fontScale              = 1.5
	fontColor              = (0,0,0)
	thickness              = 2
	lineType               = 2


	
	cv2.putText(img,"1 - Muito Mau",bottomLeftCornerOfText,font,fontScale,fontColor,thickness,lineType)
	cv2.putText(img,"2 - Mau",(bottomLeftCornerOfText[0],bottomLeftCornerOfText[1]+ 100),font,fontScale,fontColor,thickness,lineType)
	cv2.putText(img,"3 - Aceitavel",(bottomLeftCornerOfText[0],bottomLeftCornerOfText[1]+200),font,fontScale,fontColor,thickness,lineType)
	cv2.putText(img,"4 - Muito Bom",(bottomLeftCornerOfText[0],bottomLeftCornerOfText[1]+300),font,fontScale,fontColor,thickness,lineType)
	cv2.putText(img,"5 - Excelente",(bottomLeftCornerOfText[0],bottomLeftCornerOfText[1]+400),font,fontScale,fontColor,thickness,lineType)

	#Display the image
	cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)          
	cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	cv2.imshow("test",img)

	cv2.waitKey(5000)

def loadGrey():
	# Create a black image
	img = np.zeros((winH,winW,3), np.uint8)
	# Write some Text
	img.fill(128)

	#Display the image
	cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)          
	cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	cv2.imshow("test",img)
	cv2.waitKey(0)

def randomOrder():
	#first image
	global ultima_ordem
	global imagens_mae
	global lista_apresentavel
	global cars_codificadas
	global mountain_codificadas
	global horses_codificadas
	global barco_codificadas

	random.shuffle(ultima_ordem)
	#print(imagens_mae[2])
	#print(ultima_ordem[0])

	while len(ultima_ordem) < 48:
		ultima_ordem.append(ultima_ordem[0])
		ultima_ordem.append(ultima_ordem[1])
		ultima_ordem.append(ultima_ordem[2])
		ultima_ordem.append(ultima_ordem[3])

	
	for x in ultima_ordem:
		if x == 'cars':
			rand = random.randrange(0, len(cars_codificadas), 1)
			lista_apresentavel.append(cars_codificadas[rand])
			cars_codificadas = np.delete(cars_codificadas, rand)
		if x == 'horses': 
			rand = random.randrange(0, len(horses_codificadas), 1)
			lista_apresentavel.append(horses_codificadas[rand])
			horses_codificadas = np.delete(horses_codificadas, rand)
		if x == 'mountain':
			rand = random.randrange(0, len(mountain_codificadas), 1)
			lista_apresentavel.append(mountain_codificadas[rand])
			mountain_codificadas = np.delete(mountain_codificadas, rand)
		if x == 'barco':
			rand = random.randrange(0, len(barco_codificadas), 1)
			lista_apresentavel.append(barco_codificadas[rand])
			barco_codificadas = np.delete(barco_codificadas, rand)
	
def mostrarLoop():

	split = lista_apresentavel[len(lista_apresentavel)-1].split("/")
	split_final = split[1].split("_")
	split_final = str(split_final[0]) + ".png"
	loadImage(split_final, lista_apresentavel[len(lista_apresentavel)-1])
	lista_apresentavel.pop(len(lista_apresentavel)-1)
	
def nota():
	while True:
		if keyboard.is_pressed("1"):
			print("You pressed 1")
			return 1
		if keyboard.is_pressed("2"):
			print("You pressed 2")
			return 2
		if keyboard.is_pressed("3"):
			print("You pressed 3")
			return 3
		if keyboard.is_pressed("4"):
			print("You pressed 4")
			return 4
		if keyboard.is_pressed("5"):
			print("You pressed 5")
			return 5


#removePos()
randomOrder()
loadText()
while len(lista_apresentavel) >= 43:
	mostrarLoop()
	loadGrey()
	nota_final = nota()
	lista_notas.append(nota_final)
	print(lista_notas)

lista_notas.pop(0)

output_file = open('file.txt', 'w')

with open("file.txt","w") as f:
 for i in range(0, len(lista_notas)):
    # Velocity here is the list
    f.write("{0}\t{1}\n".format(lista_apresentavel[i],lista_notas[i]))

#treino
#print(imagens_mae)
#print(ultima_ordem)
#começar
cv2.destroyAllWindows()
