import os
import cv2 
import numpy as np
import pickle
from PIL import Image


#Finds path of this facetrain.py file and assigns it to BASE_DIR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR,'images')

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
#Use local binary picture recogniser(LBPH)algorithm
recogniser = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {} #Empty dict with ids inc. by 1 for each label (weeknd,niall etc)
y_labels = []
x_train = []

for root, dirs, files in os.walk(IMAGE_DIR):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root, file)
			label = os.path.basename(root).replace(" ", "-").lower() #Path cleaning to avoid errors
			print(label, path)
			if not label in label_ids:
				label_ids[label] = current_id
				current_id+=1

			id_ = label_ids[label]
			# print(label_ids)

			#PIL - Python image library(pip install pillow. Check with pip freeze)

			pil_image = Image.open(path).convert("L") #Grayscale
			image_array = np.array(pil_image, "uint8") #Turning image into a NumPy array(unsigned 8 bit integers)
			# print(image_array)

			faces = face_cascade.detectMultiScale(image_array, scaleFactor = 1.5, minNeighbors = 5)

			for (x,y,w,h) in faces:
				roi = image_array[y:y+h, x:x+w]
				x_train.append(roi)
				y_labels.append(id_)

				#To save label ids use Pickle
# print(y_labels)
# print(x_train)


with open("labels.pickle", 'wb') as f:
	pickle.dump(label_ids,f)


recogniser.train(x_train, np.array(y_labels))
recogniser.save("trainer.yml")