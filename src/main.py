import numpy as np
import cv2 as cv

'''
TODO: Create findScoreBoard()
NOTE: Threshold of 66 works fine for now
'''

''' --------PROPERTY ALIASES------------- '''
_WIDTH = cv.CAP_PROP_FRAME_WIDTH
_HEIGHT = cv.CAP_PROP_FRAME_HEIGHT
_FPS = cv.CAP_PROP_FPS
_FRAME_COUNT = cv.CAP_PROP_FRAME_COUNT 
''' --------------------------------------'''

''' Get the Test Frame '''
cap = cv.VideoCapture('fullmatch.mp4')
cap.set(cv.CAP_PROP_POS_FRAMES, 20000)
ret, img = cap.read()
cap.release()

