import cv2 as cv

class rwImagen:
    def __init__(self,ruta,nameImage="Imagen") -> None:
        self.im = cv.imread(ruta, 1)
        self.nm = nameImage 
        self.ext = ruta[ruta.find("."):len(ruta)]
    
    def mostrar(self,time=5*1000):
        cv.imshow(self.nm, self.im) 
        cv.waitKey(time)
    
    def guardar(self):
        cv.imwrite(self.nm+"Saved"+self.ext,self.im)
        print("Imagen guardada")
    
class filtrado:
    def __init__(self, ruta) -> None:
        self.imagen = rwImagen(ruta)
    
    def setrango(self,superior, inferior, rgb="None"):
        if rgb == "r":
            self.rango_rs = superior
            self.rango_ri = inferior
        
        if rgb == "g":
            self.rango_gs = superior
            self.rango_gi = inferior
        
        if rgb == "b":
            self.rango_bs = superior
            self.rango_bi = inferior
        # else:
        #     print(""" 
        #     Seleccione un valor valido para rgb: (String)
        #         "r": red
        #         "g": green
        #         "b": blue
        #     """)
    def clasificar(self):
        im = self.imagen.im

        r_s, g_s, b_s = self.rango_rs, self.rango_gs,self.rango_bs 
        r_i, g_i, b_i = self.rango_ri, self.rango_gi,self.rango_bi 

        for x in range(0,im.shape[1]):
            for y in range(0, im.shape[0]):
                b,g,r = im[y,x]
                if (r > r_i and r <= r_s)and(g > g_i and g <= g_s)and(b > b_i and b <= b_s):
                    im[y,x] = [255,255,255]
                else:
                    im[y,x] = [0,0,0]
    
    def aplicarCromatismo(self):
        im = self.imagen.im

        for y in range(0, im.shape[0]):
            for x in range(0,im.shape[1]):
                im[y,x] = self.cordenadaCromatica(im[y,x,0],im[y,x,1],im[y,x,2])
                   

    def cordenadaCromatica(self,b,g,r):
        rgb = [b,g,r]
        try:
            cro = []
            for i in rgb:
                cro.append(int((int(i)/(int(r)+int(g)+int(b)))*255))
            return cro   
        except ZeroDivisionError:
            return [0,0,0]             

    def valoresMaximoRGB(self):
        im = self.imagen.im

        Rmax = 0
        Gmax = 0
        Bmax = 0

        for y in range(0, im.shape[0]):
            for x in range(0,im.shape[1]):
                if Rmax < im[y,x,2]:
                    Rmax = im[y,x,2]
                if Gmax < im[y,x,1]:
                    Gmax = im[y,x,1]
                if Bmax < im[y,x,0]:
                    Bmax = im[y,x,0]
        return int(Bmax),int(Gmax),int(Rmax)
    
    def coordenadasWPatch(self,b,g,r,Bmax,Gmax,Rmax):
        r = int((255/Rmax)*r)
    
        g = int((255/Gmax)*g)
     
        b = int((255/Bmax)*b)

        return [b,g,r]

    def white_patch(self):
        
        im = self.imagen.im
        Bmax,Gmax,Rmax= self.valoresMaximoRGB()
        for y in range(0, im.shape[0]):
            for x in range(0,im.shape[1]):
                im[y,x] = self.coordenadasWPatch(im[y,x,0],im[y,x,1],im[y,x,2],Bmax,Gmax,Rmax)

if __name__ == "__main__":


    im = filtrado('Media/Imagen_F.jpg')
    im.imagen.nm = "Imagen Original"
    im.imagen.mostrar(0)

    #Coordenadas Normales
    # im.setrango(260,230,rgb="r")
    # im.setrango(197,170,rgb="g")
    # im.setrango(136,100,rgb="b")
    
    #Cordenadas Cromaticas
    # im.setrango(120,90,rgb="r")
    # im.setrango(97,82,rgb="g")
    # im.setrango(72,50,rgb="b")

    #Coordenadas Whitepatch
    im.setrango(255,200,rgb="r")
    im.setrango(255,166,rgb="g")
    im.setrango(190,82,rgb="b")
    

    im.white_patch()
    im.imagen.nm = "Imagen WhitePatch"
    im.imagen.mostrar(0)

    # im.aplicarCromatismo()
    # im.imagen.nm = "Imagen Cromatica"
    # im.imagen.mostrar(0)


    im.clasificar()
    im.imagen.nm = "Imagen Filtrada (Guitarra en medio)"
    im.imagen.mostrar(0)

    cv.destroyAllWindows()
