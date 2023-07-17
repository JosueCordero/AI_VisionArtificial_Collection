import numpy as np
import cv2 as cv

#Traslacion de una imagen

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# Rotar una imagen

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

if __name__ == "__main__":
    img = cv.imread("Media/Imagen_F.jpg")
    img_p = cv.imread("Media/Imagen_P.jpeg")

    img_trasladada = translate(img,100,40)
    img_rotada = rotate(img,45)

    #Resize de la imagen
    y,x = img.shape[:2]
    img_ampliada = cv.resize(img,(int(x*1.5),int(y*1.5)),interpolation=cv.INTER_CUBIC)
    
    #Cambio de perpectiva
    y,x = img_p.shape[:2]

    pts1 = np.float32([[229,161],[674,174],[0,540],[518,559]])
    pts2 = np.float32([[0,0],[520,0],[0,380],[520,380]])

    M = cv.getPerspectiveTransform(pts1,pts2)
    img_perpectiva = cv.warpPerspective(img_p,M,(520,380))

    cv.imshow("Imagen 1",img)
    cv.waitKey(0)
    cv.imshow("Imagen 2",img_p)
    cv.waitKey(0)
    cv.imshow("Imagen trasladada",img_trasladada)
    cv.waitKey(0)
    cv.imshow("Imagen rotada",img_rotada)
    cv.waitKey(0)
    cv.imshow("Imagen resize",img_ampliada)
    cv.waitKey(0)
    cv.imshow("Imagen cambio de perpectiva",img_perpectiva)

    cv.waitKey(0)
    cv.destroyAllWindows()
