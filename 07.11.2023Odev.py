"""
    02210201034 - Yüksel Caner MÜLAZIMOĞLU
    07.11.2023 tarihli 1. öğretim görüntü işleme ödevi
"""
import cv2
import numpy as np

foto = cv2.imread("foto.jpeg",0)

histogram = [0 for x in range(256)]

for i in range(len(foto[:,0])):
    for j in range(len(foto[0,:])):
        histogram[foto[i,j]] += 1

print(histogram)