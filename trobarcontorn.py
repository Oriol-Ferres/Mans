import cv2
from PIL import Image

def trobarpalmell(ampladadit, imatge, imatgeretall):
    gray_image = cv2.cvtColor(imatge, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray_image,127,255,0)

    M = cv2.moments(thresh)

    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    #p1 = (int(cX-151), int(cY-55))
    #p2 = (int(cX+105), int(cY+115))

    p1 = (int(cX-150), int(cY-60))
    p2 = (int(cX+100), int(cY+150))

    print('Centre:', cX, cY)
    print(ampladadit)

    cv2.circle(imatge, (cX, cY), 5, (255,255,255), -1)
    #palmell = int(cX-151),int(cY-55),int(cX+105),int(cY+115)
    palmell = int(cX-(ampladadit*3+3)),int(cY-(ampladadit+5)),int(cX+(ampladadit*2+5)),int(cY+(ampladadit*3+15))
    
    cv2.circle(imatge, (cX, cY), 5, (255, 255, 255), -1)
    cv2.rectangle(imatge, p1, p2, (0,0,255), 1)

    im = imatgeretall.crop(palmell)
    im.save('retall.png')
    return(im)


