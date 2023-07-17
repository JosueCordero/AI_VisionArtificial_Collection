import cv2 as cv
import numpy as np

class rwVideo:
    def __init__(self,root,nameVideo="Video",guardar=False) -> None:
        self.cap = cv.VideoCapture(root)
     
        if type(root) == int:
           
            if not self.cap.isOpened():
                print("No se pudo abrir la camara")
                exit()
        self.guardar = guardar
        if guardar:
            self.exit = cv.VideoWriter('Video_Guardado.mkv',cv.VideoWriter_fourcc(*'XVID'),20.0,(int(self.cap.get(3)),int(self.cap.get(4))))
       
    def canny(self,frame):
        im = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        canny = cv.Canny(im,100,200)
        canny =  cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
        return canny

    def prewitt(self,frame):
        im = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        kernelx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]]) 
        img_prewitt_x = cv.filter2D(im, -1, kernelx)
        img_prewitt_y = cv.filter2D(im, -1, kernely)

        img_prewitt = img_prewitt_x + img_prewitt_y
        img_prewitt = cv.cvtColor(img_prewitt, cv.COLOR_GRAY2BGR)

        return img_prewitt
    
    def sobel(self,frame):
        im = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        img_sobelx = cv.convertScaleAbs(cv.Sobel(im,cv.CV_64F,1,0,ksize=3))
        img_sobely = cv.convertScaleAbs(cv.Sobel(im,cv.CV_64F,0,1,ksize=3))
        
        img_sobel = img_sobelx + img_sobely
        img_sobel = cv.cvtColor(img_sobel, cv.COLOR_GRAY2BGR)

        return img_sobel

    def laplaciano(self,frame):
        im = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        img_laplaciano = cv.convertScaleAbs(cv.Laplacian(im,cv.CV_64F,ksize=3))

        img_laplaciano = cv.cvtColor(img_laplaciano, cv.COLOR_GRAY2BGR)

        return img_laplaciano

    def laplaciano_gauss(self,frame):
        frame = cv.GaussianBlur(frame,(5,5),0)
        return self.laplaciano(frame)


    def mostrarVideo(self,filter=None):
        guardar = self.guardar
        print("Para salir del video presione: d")

        while True:
            istrue, frame = self.cap.read()
           
            if istrue:
                if filter:
                    frame = filter(frame)

                cv.imshow('Video', frame)
                if guardar:
                    self.exit.write(frame)
                if cv.waitKey(20) & 0xFF==ord('d'):
                    break            
            else:
                break
        
        self.cap.release()
        if guardar:
            print("Video Guardado")
            self.exit.release()
        cv.destroyAllWindows() 

if __name__ == "__main__":
    filtervideo = rwVideo(0,nameVideo="Filtro Canny",guardar=True)
    filtervideo.mostrarVideo(filter=filtervideo.laplaciano_gauss)
