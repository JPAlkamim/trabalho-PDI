import numpy as np
import cv2 as cv


def ajustarBrilho(img, limiarT, acima, brilho):  
    if not acima:
        indicesVetor = img < limiarT
    else:
        indicesVetor = img >= limiarT


    img = img.astype(int)
    if brilho > 0:
      img[indicesVetor] = np.minimum(255, img[indicesVetor] + brilho,)
    else:
      img[indicesVetor] = np.maximum(0, img[indicesVetor] + brilho)

    img = img.astype(np.uint8)
    cv.imshow('Resultado',img)
    
    
def pegarParametros():
    img  = cv.imread('./taylor.jpg', 0)
    limiarT = int(input("Valor da Limiar T (entre 0 até 255) = "))
    acima = int(input("Quer que seja acima do limite? Digite 10, caso contrário 0 = "))
    if(acima < 10):
        acima = False
    else:
        acima = True
    brilho = int(input("Número para aumento ou diminuição de brilho (positivos ou negativos) = "))
    return img, limiarT, acima, brilho
    

if __name__ ==  '__main__':
    img , limiarT, acima, brilho = pegarParametros()
    ajustarBrilho(img, limiarT, acima, brilho)