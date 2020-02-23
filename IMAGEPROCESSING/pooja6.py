'''import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("img.jpeg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.01, minNeighbors=5)

for x,y,w,h in faces:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows'''

import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(r"faceDetection.mp4")
check =True
while check:
	check, frame =video.read()

	gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.25, minNeighbors=14)

	for x,y,w,h in faces:
		frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

		cv2.imshow("Gray",frame)
		cv2.waitKey(1)

cv2.destroyAllWindows()

video.release()


	

