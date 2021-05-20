##fa linies gordes i les posa a la imatge negre
##
##
##
##
import cv2
import PIL
import numpy as np
def dibuixargruixut(img):

    #img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)

    #img = cv2.equalizeHist(img)
    #cv2.imwrite('./retall.png', img)

    #img = cv2.GaussianBlur(img, (1,1),0)

    img = cv2.Canny(img, 70, 70)

    #cv2.imshow('',img)
    #cv2.waitKey(0)


    lineat = cv2.imread('./fondo.png')
    linies = cv2.HoughLinesP(img, 1, np.pi / 180, 15, np.array([]),50,20)
    for linea in linies:
        for x1,y1,x2,y2 in linea:
            cv2.line(lineat, (x1,y1),(x2,y2), (255,255,255), 7)
            
    cv2.imwrite('./liniesgruixudes.png', lineat)

