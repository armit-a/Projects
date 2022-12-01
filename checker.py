import numpy as np
import cv2
img = np.zeros((800,800,3))
xn=0

for x in range(1,9):
    
    yn=0
    for y in range(1,9):
        if((x+y)%2==0):
            img[xn*100:x*100,yn*100:y*100]=255,255,255
            yn=y
            
        else:
            img[xn*100:x*100,yn*100:y*100]=0,0,0
            yn=y
    xn=x 


cv2.imshow('CHECKER BOARD',img)
cv2.waitKey(0)
cv2.DestroyAllWindows()
