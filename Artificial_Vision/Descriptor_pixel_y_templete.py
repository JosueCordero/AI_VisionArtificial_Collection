import cv2 as cv
import p1_19310395_va as va

def clasificar_show():
    im.clasificar()
    im.imagen.nm = "Imagen Filtrada (Guitarra en medio)"
    im.imagen.mostrar(0)

def imagen():
    im = va.filtrado('Media/Imagen_F.jpg')
    im.imagen.nm = "Imagen Original"
    im.imagen.mostrar(0)

    return im

if __name__ == "__main__":
  

    a = input("""
        Que es lo que deseas hacer?
        1)Descriptor simple
        2)Descriptor simple (Cordenadas cromaticas)
        3)Descriptor simple (Cordenadas whitepatch)
        4)Templete maching
    """)

    if a == '1':
        im = imagen()
        #Coordenadas Normales
        im.setrango(260,230,rgb="r")
        im.setrango(197,170,rgb="g")
        im.setrango(136,100,rgb="b")

        clasificar_show()
    if a == '2': 
        im = imagen()
        #Cordenadas Cromaticas
        im.setrango(120,90,rgb="r")
        im.setrango(97,82,rgb="g")
        im.setrango(72,50,rgb="b")
        
        im.aplicarCromatismo()
        im.imagen.nm = "Imagen Cromatica"
        im.imagen.mostrar(0)

        clasificar_show()

    if a == '3':
        im = imagen()
        #Coordenadas Whitepatch
        im.setrango(255,200,rgb="r")
        im.setrango(255,166,rgb="g")
        im.setrango(190,82,rgb="b")
        
        im.white_patch()
        im.imagen.nm = "Imagen WhitePatch"
        im.imagen.mostrar(0)

        clasificar_show()

    if a == '4':
        #Templete maching

        imagen = va.templete("Media/Imagen_F.jpg","Media/Imagen_F_temp_3.png")
        imagen.findTemplete()
        imagen.dibujarRectangulo((255,255,255))
        imagen.graficar()
   

    
    cv.destroyAllWindows()

    