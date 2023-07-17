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

class rwVideo:
    def __init__(self,ruta,nameVideo="Video") -> None:
        self.cap = cv.VideoCapture(ruta)
        self.exit = cv.VideoWriter('Video_Guardado.mkv',cv.VideoWriter_fourcc(*'XVID'),20.0,(int(self.cap.get(3)),int(self.cap.get(4))))
    
    def mostrarVideo(self,guardar=False):
        while True:
            istrue, frame = self.cap.read()
            if istrue:
                cv.imshow('Video', frame)
                if guardar:
                    self.exit.write(frame)
                if cv.waitKey(20) & 0xFF==ord('d'):
                    break            
            else:
                break
        if guardar:
            print("Video Guardado")
        self.cap.release()
        self.exit.release()
        cv.destroyAllWindows()  

if __name__ == "__main__":
    imagen = rwImagen("Media/imagen.png",nameImage="Imagen Mandalorian")
    imagen.mostrar()
    imagen.guardar()
    video = rwVideo('Media/Video.mkv',nameVideo="Video Foo Fighters")
    video.mostrarVideo(guardar=True)