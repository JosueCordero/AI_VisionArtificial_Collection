from json.tool import main
from unicodedata import name
import cv2 as cv
import numpy as np
from skimage.util import random_noise
import random

def rezise(scale,img):
    width = int(img.shape[1] * scale)
    heigth = int(img.shape[0] * scale)
    dim = (width,heigth)
    return cv.resize(img,dim, interpolation=cv.INTER_AREA)


if __name__ == "__main__":
    #Imagen Origianal
    img = cv.imread("Media/Imagen_F.jpg",1) 

    #Imagen con Ruido Gaussiano 
    noise_img_G = random_noise(img,mode='gaussian',seed=None,clip=True)
    noise_img_G = np.array(255*noise_img_G,dtype='uint8')

    #Imagen con ruido sal y pimienta
    noise_img_sp = random_noise(img,mode='s&p',amount=0.05)
    noise_img_sp = np.array(255*noise_img_sp,dtype='uint8')

    imagenes = [[img,"Orginal"], [noise_img_G, "Ruido Gaussiano"],[noise_img_sp,"Ruido sal y pimienta"]]

    #Imagen en blanco (Uso exclusivo para imprmir)
    y,x = img.shape[:2]
    blank_img = 255*np.ones((y,x,3),np.uint8)

    for imagen, nm in imagenes:
        #Filtro Promedio
        promedio = cv.blur(imagen,(3,3))
        #Filtro Gaussiano
        gaussiano = cv.GaussianBlur(imagen,(5,5),0)
        #Filtro de la Mediana
        mediana = cv.medianBlur(imagen,3)
        #Filtro Maximo
        kernelMm = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
        maximo = cv.dilate(imagen,kernelMm)
        #Filtro Minimo
        minimo = cv.erode(imagen,kernelMm)

        res = cv.vconcat([cv.hconcat([imagen,gaussiano]),cv.hconcat([mediana,blank_img])])
        res1 = cv.vconcat([cv.hconcat([imagen,promedio]),cv.hconcat([maximo,minimo])])
        #res = rezise(.8,res)
        cv.imshow(F"Imagen {nm} con Filtros lineales (Gaussiano,mediana)",res)
        cv.waitKey(0)
        cv.imshow(F"Imagen {nm} con Filtros no lineales (promedio, maximo, minimo)",res1)
        cv.waitKey(0)
        cv.destroyAllWindows()