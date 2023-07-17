import cv2 as cv
import numpy as np


if __name__ == "__main__":

    img = cv.imread('Media/Imagen_F.jpg',cv.IMREAD_GRAYSCALE)
    img_gaussian = cv.GaussianBlur(img,(5,5),0)

    #Prewitt
    kernelx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]]) 
    img_prewitt_x = cv.filter2D(img, -1, kernelx)
    img_prewitt_y = cv.filter2D(img, -1, kernely)

    img_prewitt = img_prewitt_x + img_prewitt_y

    #Sobel

    img_sobelx = cv.convertScaleAbs(cv.Sobel(img,cv.CV_64F,1,0,ksize=3))
    img_sobely = cv.convertScaleAbs(cv.Sobel(img,cv.CV_64F,0,1,ksize=3))

    img_sobel = img_sobelx + img_sobely

    #Laplaciano 
    
    img_laplaciano = cv.convertScaleAbs(cv.Laplacian(img,cv.CV_64F,ksize=3))

    #Laplaciano con filtro gausseano

    img_laplaciano_G = cv.convertScaleAbs(cv.Laplacian(img_gaussian,cv.CV_64F,ksize=3))

   
    cv.imshow("Filtro Prewitt X", img_prewitt_x)
    cv.imshow("Filtro Prewitt Y", img_prewitt_y)
    cv.imshow("Filtro Prewitt", img_prewitt)
    cv.imshow("Imagen Original", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    
    cv.imshow("Filtro Sobel X", img_sobelx)
    cv.imshow("Filtro Sobel Y", img_sobely)
    cv.imshow("Filtro Sobel", img_sobel)
    cv.imshow("Imagen Original", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imshow("Filtro Laplaciano", img_laplaciano)
    cv.imshow("Filtro Laplaciano con filtro Gussiano", img_laplaciano_G)
    cv.imshow("Imagen Original", img)
    cv.waitKey(0)
    cv.destroyAllWindows()