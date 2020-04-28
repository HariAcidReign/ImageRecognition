import os
import numpy as np
import cv2

filename = 'videorec.mp4'
fps = 24.0
my_res = '720p'

def change_res(cap,width,height):
	cap.set(3,width)
	cap.set(4,height)

STD_DIMENSIONS = {
	"480p": (640,480),
	"720p": (1280,720),
	"1080p": (1920,1080),
	"4k": (3840,2160)
}

def get_dims(cap, res='1080p'):
	width,height = STD_DIMENSIONS['480p']
	if res in STD_DIMENSIONS:
		width,height = STD_DIMENSIONS[res]
	change_res(cap,width,height)
	return width,height

VIDEO_TYPE = {
	'avi': cv2.VideoWriter_fourcc(*'XVID'),
	'mp4': cv2.VideoWriter_fourcc(*'XVID')
}

def get_video_type(filename):
	filename, ext = os.path.splitext(filename)
	if ext in VIDEO_TYPE:
		return VIDEO_TYPE[ext]
	return VIDEO_TYPE['avi']

cap = cv2.VideoCapture(0) 
# VideoCapturing from the laptop webcam
dims = get_dims(cap, res = my_res)


# Making 480p videos
# def make_480p():
# 	cap.set(3,640)
# 	cap.set(4,480)
# make_480p()

# For 1080p videos
# def make_1080p():
# 	cap.set(3,1920)
# 	cap.set(4,1080)

# make_1080p()

# To rescale the frame into anything of choice
# def rescale_frame(frame, percent = 75):
# 	scale_percent = 75
# 	width = int(frame.shape[1] * scale_percent / 100)
# 	height = int(frame.shape[0] * scale_percent / 100)
# 	dim = (width, height)
# 	return cv2.resize(frame,dim,interpolation = cv2.INTER_AREA)

video_type_cv2 = get_video_type(filename)

out = cv2.VideoWriter(filename, video_type_cv2, fps, dims)

while True:
	ret, frame = cap.read()
	# Reads data frame by frame
	# frame = rescale_frame(frame, percent = 40)
	# To resize what the webcam shows
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Color conversion into grayscale
	out.write(frame)
	cv2.imshow('frame', frame) 
	# cv2.imshow('gray', gray) 
	# Shows the photo.Note: Its not imgshow
	if cv2.waitKey(20) & 0xFF == ord('q'):
   	    sbreak
   	    # Closes the frame on pressing q

# out.release()