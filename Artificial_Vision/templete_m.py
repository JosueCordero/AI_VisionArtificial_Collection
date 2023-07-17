import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

class rwImagen:
    def __init__(self,ruta,nameImage="Imagen",scaleColor=1) -> None:
        self.im = cv.imread(ruta, scaleColor)
        self.nm = nameImage 
        self.ext = ruta[ruta.find("."):len(ruta)]
    
    def mostrar(self,time=5*1000):
        cv.imshow(self.nm, self.im) 
        cv.waitKey(time)
    
    def guardar(self):
        cv.imwrite(self.nm+"Saved"+self.ext,self.im)
        print("Imagen guardada")


class templete:
    def __init__(self, ruta_img, ruta_templete):
        self.imagen = rwImagen(ruta_img,scaleColor=0)
        self.templete = rwImagen(ruta_templete,scaleColor=0)
        self.templete_two = rwImagen(ruta_templete,scaleColor=1)
        self.imagen_two =  rwImagen(ruta_img,scaleColor=1)
        self.img = self.imagen.im
        self.temp = self.templete.im
        self.img_two = self.imagen_two.im
        self.temp_two = self.templete_two.im
        #Resolver
        self.alto, self.largo = self.temp.shape[:2]

    def encontrarTemplete(self):
        
            self.res = self.findTemplete(self.img, self.temp)
            
            #Ver si las dejo nadamas como funciones
            self.dibujarRectangulo((255,255,255))
            self.graficar()

    def dibujarRectangulo(self,colorRGB):
        val_min, val_max, min_loc, max_loc = cv.minMaxLoc(self.res)
        ubi = min_loc
        inf_der = (ubi[0] + self.largo, ubi[1] + self.alto)
        cv.rectangle(self.img_two, ubi, inf_der, colorRGB, 3)

    def graficar(self):
        plt.figure("Maximos y minimos de una imagen",figsize=(8,4))
        plt.imshow(self.res, cmap='gray')
        

        cv.imshow('Imagen', self.img_two)
        cv.imshow('Template',  self.temp_two)

       
        cv.waitKey(0)
        plt.show()
        cv.destroyAllWindows()

    def findTemplete(self,img=None,temp=None):
            if img == None or temp==None:
                img = self.img
                temp = self.temp

            temp = temp.astype('int')
            alto, largo = temp.shape[:2]
            m_img = img[:alto,:largo]
            m_img = m_img.astype('int')
    
            y_temp, x_temp = temp.shape[:2]
            y_img, x_img = img.shape[:2]

            cy_temp = int(y_temp/2)
            cx_temp = int(x_temp/2)

            res = np.zeros((y_img-y_temp+1,x_img-x_temp+1))
            y_res = range(0,res.shape[0]).__iter__()
            
            for y in range(cy_temp, y_img-(y_temp-cy_temp-1)):
                m_img2 = m_img
                x_res = range(0,res.shape[1]).__iter__()
                yr = next(y_res)
                for x in range(cx_temp, x_img-(x_temp-cx_temp-1)):
                    
                    xr = next(x_res)
                    res[yr,xr]= np.sum((temp-m_img2)**2)
                    m_img2 = np.delete(m_img2,0,axis=1)
                    if y_temp%2 == 0:
                        m_img2 = np.append(m_img2,img[y-cy_temp:y+cy_temp,x+cx_temp:x+cx_temp+1],axis=1)
                    else:
                        m_img2 = np.append(m_img2,img[y-cy_temp:y+cy_temp+1,x+cx_temp:x+cx_temp+1],axis=1)
                
                m_img = np.delete(m_img,0,axis=0)

                try:
                    m_img = np.append(m_img,[img[y+cy_temp][0:largo]],axis=0)
                except IndexError:
                    pass
            
            self.res = res        
            return res

if __name__ == "__main__":
    imagen = templete("Media/Imagen_F.jpg","Media/Imagen_F_temp_3.png")
    imagen.findTemplete()
    imagen.dibujarRectangulo((255,255,255))
    imagen.graficar()





    # img = cv.imread('Media/Imagen_F.jpg',0) # El 0 convierte a escala de grises
    # temp = cv.imread('Media/Imagen_F_temp_3.png',0)

    # alto, largo = temp.shape[:2]
    # res = findTemplete(img,temp)
    # v_min, v_max, l_min, l_max = cv.minMaxLoc(res)
    # ubi = l_min

    # img2 = cv.imread("Media/Imagen_F.jpg")
    # temp = cv.imread("Media/Imagen_F_temp_3.png")


    # inf_der = (ubi[0] + largo, ubi[1] + alto)
    # cv.rectangle(img2, ubi, inf_der, (255, 0, 150), 3)

    # cv.imshow('Imagen', img2)
    # cv.imshow('Template', temp)
    # cv.waitKey(0)
                
    # cv.destroyAllWindows()