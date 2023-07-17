import cv2 as cv
import numpy as np

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
    
class templeteMatching:
    def __init__(self, ruta, rutaTemp) -> None:
        self.imagen = rwImagen(ruta)
        self.templete = rwImagen(rutaTemp)
    
    def findTemplete(self):
        y_temp, x_temp = self.templete.shape[:2]
        y_img, x_img = self.imagen.shape[:2]

        cy_temp = int(y_temp/2)
        cx_temp = int(x_temp/2)

        res = np.zeros((y_img-y_temp+1,x_img-x_temp+1))
        y_res = range(0,res.shape[0]).__iter__()
        

        for y in range(cy_temp, y_img-(y_temp-cy_temp-1)):
            x_res = range(0,res.shape[1]).__iter__()
            yr = next(y_res)
            for x in range(cx_temp, x_img-(x_temp-cx_temp-1)):
                xr = next(x_res)
                res[yr,xr]=self.disimilitud(y,x,self.imagen,self.templete)
        
        return res

    def disimilitud(self,yi,xi,img,temp):
        sum = 0

        y_yp = range(yi-(temp.shape[0]-1)).__iter__()
       

        for yp in range(0,temp.shape[0]):
            x_xp = range(xi-(temp.shape[1]-1)).__iter__()
            y_img = next(y_yp)

            for xp in range(0,temp.shape[1]):
                sum += (int(temp[yp,xp])-int(img[y_img,next(x_xp)]))**2
        
        return sum
                
            
if __name__ == "__main__":
    pass