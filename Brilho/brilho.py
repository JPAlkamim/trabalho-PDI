import numpy as np
import cv2 as cv


def ajustarBrilho(img, limiarT, acima, brightness):  
    if acima:
        indicesVetor = img >= limiarT
    else:
        indicesVetor = img < limiarT


    img = img.astype(int)
    if brightness > 0:
      img[indicesVetor] = np.minimum(img[indicesVetor] + brightness, 255)
    else:
      img[indicesVetor] = np.maximum(img[indicesVetor] + brightness, 0)

    img = img.astype(np.uint8)
    cv.imshow('Resultado',img)
    
    
def pegarParametros():
    img  = cv.imread('./reputation.jpg', 0)
    limiarT = int(input("Valor da Limiar T (entre 0 até 255) = "))
    acima = int(input("Quer que seja acima do limite? Digite 1, caso contrário 0 = "))
    if(acima < 1):
        acima = False
    else:
        acima = True
    brilho = int(input("Número para aumento ou diminuição de brilho (positivos ou negativos) = "))
    return img, limiarT, acima, brilho
    

if __name__ ==  '__main__':
    img , limiarT, acima, brilho = pegarParametros()
    ajustarBrilho(img, limiarT, acima, brilho)