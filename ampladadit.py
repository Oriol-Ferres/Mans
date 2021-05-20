import cv2
import imutils
from PIL import Image

def ampladadeldit(imatgeeditar, imatgevalors):

    gray_image = cv2.cvtColor(imatgevalors, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray_image,120,255,0)

    #cv2.imwrite('./mabinari.png', thresh)
    #cv2.waitKey(0)
    
    #imatge = Image.open('./mabinari.png').convert('RGB')
    #imatgepix = imatge.load()
    
    contorn = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = imutils.grab_contours(contorn)
    c = max(cnt, key=cv2.contourArea)

    #colorets = tuple((0,255,0))

    #for a in contorn:
    #    for b in c:
    #        for d in c:
    #            for e, f in d:
    #                e = int(e)
    #               f = int(f)
    #               imatgepix[e, f] = (255,0,0)
                    
                    

    #imatge.save('./probadetrobarcontorns.png')



    
    amunt=tuple(c[c[:,:, 1].argmin()][0])

    cv2.circle(imatgevalors, amunt,1, (0,0,255), -1)
    cv2.rectangle(imatgevalors, (amunt[0]-35, amunt[1]+10), (amunt[0]+35, amunt[1]), (255,0,0), 1)
    ##
    ditmig = (amunt[0]-35,amunt[1],amunt[0]+60,amunt[1]+25)

    im1 = imatgeeditar.crop(ditmig)
    im1.save('./ditmig.png')

    #cv2.imshow('', imatgevalors)
    #cv2.waitKey(0)
    ########################

    dmig = cv2.imread('./ditmig.png')
    dmig_gris = cv2.cvtColor(dmig, cv2.COLOR_BGR2GRAY)
    dmigret,dmigthresh = cv2.threshold(dmig_gris,127,255,0)

    contorndmig = cv2.findContours(dmigthresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntdmig = imutils.grab_contours(contorndmig)
    cdmig = max(cntdmig, key=cv2.contourArea)

    esquerra = tuple(cdmig[cdmig[:,:, 1].argmax()][0])
    dreta = tuple(cdmig[cdmig[:,:, 0].argmax()][0])

    #print(esquerra, dreta)

    cv2.circle(dmig, esquerra,1, (255,0,0), -1)
    cv2.circle(dmig, dreta,1, (255,0,0), -1)

    ampladadit = dreta[0]-esquerra[0]

    return(ampladadit)



