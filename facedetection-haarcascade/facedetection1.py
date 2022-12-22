import cv2
from cv2 import CV_32F


xml_haar_cascade = 'haarcascade_frontalface_alt2.xml'

#carregar classificador
faceClassfier = cv2.CascadeClassifier(xml_haar_cascade)

#carregar camera
capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while not cv2.waitKey(20) & 0xFF == ord("q"):

 ret, frame_color = capture.read()

 gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)

 faces = faceClassfier.detectMultiScale(gray)

 for x, y, w, h in faces:
     cv2.rectangle(frame_color, (x, y), (x + w, y + h), (0,0,225), 2 )

 cv2.imshow('Bruno facedetection', frame_color)
 cv2.imshow('gray camera test', gray)