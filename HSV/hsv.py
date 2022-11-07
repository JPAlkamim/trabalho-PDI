import numpy as np
import cv2 as cv


def novaImagem(img, matiz, x):
    H,S,V = cv.split(img)
    inicio = np.mod((matiz - x) / 2, 180)
    fim = np.mod((matiz + x) / 2, 180)
    intervaloInicio = H >= inicio
    intervaloFim = H < fim
    if (fim > inicio):
        indices = intervaloInicio & intervaloFim
    else: 
        indices = intervaloInicio | intervaloFim
    H = H.astype(np.uint16)
    H[indices] = np.mod(H[indices] + 90, 180).astype(np.uint8)
    H = H.astype(np.uint8)
    return cv.merge([H,S,V])

def pegarParametros():
    img  = cv.imread('./lover.jpg')
    matiz = int(input("Valor inteiro de Matiz (0 <= m < 360) = "))
    x = int(input("Valor de X = "))
    return img, matiz, x
    
    
if __name__ ==  '__main__':
    img, matiz, x = pegarParametros()
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    HSV = novaImagem(img, matiz, x)
    img = cv.cvtColor(HSV, cv.COLOR_HSV2BGR)
    cv.imshow("Resultado", img)
    