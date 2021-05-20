import cv2
from PIL import Image
import numpy as np
import math

#Obrir la imatge en opencv i pil
imatgeopencv = cv2.imread('./liniesgruixudes.png')
imatgepil = Image.open('./liniesgruixudes.png')

def ferlinies(img, imged):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    px = imged.load()
    ma = cv2.imread('./retall.png')

    contorns, hirecrachy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    def separarcontorns(contorns):
        llista = []
        for i in contorns:
            for z, q in i:
                z = int(z)
                q = int(q)
                llista.append([z, q])
        print(type(llista))
        return(llista)

    def lineaf(contorn):
        centre = int(len(contorn)/2)
        extrem1 = tuple(contorn[0])
        extrem2 = tuple(contorn[centre])
        ###Dibuixar cercles
        cv2.circle(ma, extrem1,3,(0,0,255),-1)
        cv2.circle(ma, extrem2,3,(0,255,0),-1)
        ##Agafar el centre i
        x1 = int(extrem1[0])
        y1 = int(extrem1[1])
        x2= int(extrem2[0])
        y2= int(extrem2[1])

        centrex = int((x1+x2)/2)
        centrey = int((y1+y2)/2)

        centre = tuple([centrex, centrey])
        #cv2.circle(ma, centre,3,(0,0,255),-1)
        return([extrem1, extrem2], [centrex, centrey])
        return([centrex, centrey])

    def graus(linea):
        mig = int(len(linea)/2)
        x1 = linea[0][0]
        y1 = linea[0][1]

        x2 = linea[mig][0]
        y2 = linea[mig][1]

        xd = x1 - x2
        yd = y1 - y2

        radiants = math.atan2(yd, xd)
        graus = math.degrees(radiants)
        return((int(graus))*-1) 
        
    llistaliniespr = []
    llistaliniesfin = []
    llistacentres = []
    for i in range(len(contorns)):
        a = separarcontorns(contorns[i])
        a = lineaf(a)
        linea = tuple(a[0])
        llistaliniespr.append(linea[0])
        llistaliniesfin.append(linea[1])
        centre = tuple(a[1])
        llistacentres.append(centre)
        print(linea[0], linea[1])
        cv2.line(ma, linea[0], linea[1], (255,0,0),1)
        cv2.circle(ma, centre, 3, (255,0,0,), -1)
        print(graus(a[0]) ,'º')
    llistacentres.sort()
    for i in range(len(llistacentres)):
        if i != 0:
            cv2.line(ma, llistacentres[i-1], llistacentres[i], (0,255,0),1)

    llistaliniespr.sort()
    llistaliniesfin.sort()  
    for i in range(len(llistaliniesfin)):
        if i != 0:
            cv2.line(ma, llistaliniesfin[i], llistacentres[i-1], (255,0,255),1)
    cv2.imshow('', ma)
    cv2.waitKey(0)

#ferlinies(imatgeopencv, imatgepil)



