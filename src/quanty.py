# Quantizaciòn de SubBandas
import numpy as np
import cv2
import time

def quantization(prefix,step):
    print("****************************************")
    print("Quantificar Sub-bandas")
    print("****************************************")
    image = cv2.imread(prefix, -1)

    #print("Valor de la Subbanda")
    #print(image)

    print("Quantizacion de la Subanda:",prefix)
    image=(np.array([image])/step)*step
    print(image)
    
quantization("/tmp/LH000.png",60)
quantization("/tmp/HH000.png",60)
quantization("/tmp/HL000.png",60)
quantization("/tmp/LH002.png",60)
quantization("/tmp/HH002.png",60)
quantization("/tmp/HL002.png",60)



