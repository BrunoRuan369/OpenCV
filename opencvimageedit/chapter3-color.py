import cv2
import numpy as np

#configurar imagem a ser modificada.
img = cv2.imread("Resources/img.png")
kernel = np.ones((5,5),np.uint8)

#configurar funçoes de modificaçoes.
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#deixando a imagem marrom
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)#colocando blur na imagem
imgCanny = cv2.Canny(img,150,200)#engrossar as linhas
imgDialation = cv2.dilate(imgCanny,kernel,iterations=5)#dilatar a imagem
imgEroded = cv2.erode(imgDialation,kernel, iterations=5)

#gerar cada imagem com o cv2.imshow.
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilate Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)

#setar tempo de exibiçao.
cv2.waitKey(0)