# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:38:57 2018

@author: Rads Gupta
"""

import cv2
print(cv2.__version__)
myimage=cv2.imread(r"C:\Users\Rads Gupta\Desktop\pp.jpg",cv2.IMREAD_GRAYSCALE)
print(type(myimage))
print(myimage.shape)
print(myimage.ndim)
print(myimage)
cv2.imshow("mywindow",myimage)
k=cv2.waitKey(0)&0xff
if k==27:
     cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite(r"C:\Users\Rads Gupta\Desktop\pp1.jpg",myimage)
    cv2.destroyAllWindows()
    #first it will save and then will destroy  