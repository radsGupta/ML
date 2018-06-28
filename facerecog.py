

import numpy as np
import cv2
myimage=cv2.imread(r"C:\Users\Rads Gupta\Desktop\fam.jpg")
facecascade=cv2.CascadeClassifier(r"C:\Users\Rads Gupta\Anaconda3\pkgs\opencv-3.4.1-py36_200\Library\etc\haarcascades\haarcascade_frontalface_default.xml")
eyecascade=cv2.CascadeClassifier(r"C:\Users\Rads Gupta\Anaconda3\pkgs\opencv-3.4.1-py36_200\Library\etc\haarcascades\haarcascade_eye.xml")
gray=cv2.cvtColor(myimage,cv2.COLOR_BGR2GRAY)
faces=facecascade.detectMultiScale(gray,1.3,5)
print(faces)
for(x,y,w,h) in faces:
    cv2.rectangle(myimage,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray=gray[y:y+h, x:x+w]
    roi_color=myimage[y:y+h,x:x+w]
    eyes=eyecascade.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
cv2.imshow("mywindow",myimage)
cv2.waitKey(0)
cv2.destroyAllWindows()