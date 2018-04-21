import numpy as np
import cv2 as cv

'''
TODO: Create findScoreBoard()
NOTE: Threshold of 66 works fine for now
'''

''' -------VIDEO PROPERTY ALIASES--------- '''
_WIDTH = cv.CAP_PROP_FRAME_WIDTH
_HEIGHT = cv.CAP_PROP_FRAME_HEIGHT
_FPS = cv.CAP_PROP_FPS
_FRAME_COUNT = cv.CAP_PROP_FRAME_COUNT 
''' --------------------------------------'''

''' Helper functions '''
def show(image):
    cv.imshow('FRAME', image)
    cv.waitKey(0)
    cv.destroyAllWindows()


''' Get the Test Frame '''
cap = cv.VideoCapture('../videos/test2.mp4')
# cap.set(cv.CAP_PROP_POS_FRAMES, 20000)
ret, img = cap.read()
cap.release()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def getBoundingBoxes():
    # Check top left corner to reduce the computatio
    top_third = gray[0:gray.shape[0]//5, 0:gray.shape[1]//2]
    ret, thresh = cv.threshold(top_third, 66, 255, cv.THRESH_BINARY_INV)

    # Do Morphological operations to isolate the scoreboard
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15,15))
    d = cv.dilate(thresh, kernel, iterations=1)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (21,21))
    e = cv.erode(d, kernel, iterations=1)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (17,17))
    d = cv.dilate(e, kernel, iterations=1)

    im2, contours, hierarchy = cv.findContours(d, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    boxes = []
    for i in range(len(contours)):
        x,y,w,h = cv.boundingRect(contours[i])
        # cv.rectangle(img, (x,y), (x+w,y+h), (0,255, 20), 2)
        boxes.append((x,y,w,h))

    return boxes


for b in getBoundingBoxes():
    cv.rectangle(img, (b[0],b[1]), (b[0]+b[2],b[1]+b[3]), (0,255, 20), 2)


show(img)
cv.waitKey(0)
cv.destroyAllWindows()