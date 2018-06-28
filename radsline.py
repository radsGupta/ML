

import numpy as np
import cv2
images=np.zeros((512,512,3),np.uint8)
myimage=cv2.line(images,(0,0),(511,511),(0,0,255),150)
cv2.imshow("mywindow",myimage)
cv2.waitKey(0)
cv2.destroyAllWindows()