import cv2
import numpy

cv2.namedWindo("preview")
vc = cv2.VideoCapture(0)

# Try reading first frame
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")