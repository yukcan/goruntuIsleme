import cv2
import numpy as np

foto = cv2.imread("p.jpg")
foto = cv2.cvtColor(foto,cv2.COLOR_BGR2GRAY)

ret, siyahBeyazFoto = cv2.threshold(foto, 50, 255, 0)

contours, hierarchy  = cv2.findContours(siyahBeyazFoto, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Görseldeki pirinç sayısı: ",len(contours))
cv2.imshow("originalFoto",foto)
cv2.imshow("siyahBeyazFoto",siyahBeyazFoto)
cv2.waitKey()
