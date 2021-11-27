import cv2
x=cv2.imread('image_name1.png')
y=cv2.imread('image_name2.png')
#for combining we need hstack so lets import numpy for that
import numpy as np
final=np.hstack((x,y))
cv2.imshow('hi',final)
cv2.waitKey()
cv2.destroyAllWindows()
#for saving the combined image
cv2.imwrite('any_name.png',final)
