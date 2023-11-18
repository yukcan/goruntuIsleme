import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while (True):
    ret, video = kamera.read()
    hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    lower=np.array([0, 100, 20])
    upper=np.array([10, 255, 255])

    maske=cv2.inRange(hsv,lower,upper)

    cv2.imshow("kamera", video)
    cv2.imshow("sonuc",maske)

    if cv2.waitKey(50) & 0xFF == ord('x'):
        break

kamera.release()
cv2.destroyAllWindows()