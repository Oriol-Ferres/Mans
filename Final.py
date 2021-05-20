import cv2
from PIL import Image
import os
from ampladadit import ampladadeldit
from trobarcontorn import trobarpalmell
from liniesgruixudes import dibuixargruixut
from liniesentremig import ferlinies

imatgeeditar = Image.open('./ma.png')
imatge = cv2.imread('./ma.png')

ampladadit = ampladadeldit(imatgeeditar, imatge)
trobarpalmell(ampladadit, imatge, imatgeeditar)

palmell = cv2.imread('./retall.png')
palmellgris = cv2.imread('./retall.png', cv2.IMREAD_GRAYSCALE)

dibuixargruixut(palmellgris)

gruixcv = cv2.imread('./liniesgruixudes.png')
gruixpil = Image.open('./liniesgruixudes.png')

ferlinies(gruixcv, gruixpil)



