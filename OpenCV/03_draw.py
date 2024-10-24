import cv2 as cv
import numpy as np

# Load an image from a file
img = cv.imread("C:\\Users\\Admin\\Downloads\\th.jpg")
cv.imshow('Box-Image', img)

# Create a blank image
# 500x500 is the size, 'uint8' is the data type for the image. 3 means it's a color image (RGB).
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank-img', blank)

# Change the color of the blank image to green
# Set the entire image to green (0, 255, 0) which represents the RGB color values.
'''blank[:] = 0, 255, 0
cv.imshow('Green-image', blank)'''

# Draw a rectangle
# 'blank' is the image where the rectangle is drawn. (0,0) is the top-left corner (x, y) coordinates. 
# (250, 250) is the bottom-right corner (x, y). (0, 255, 0) is the color (green).
# 'thickness' is the border thickness. Use thickness=-1 to fill the rectangle.
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

# Draw a circle
# The center of the circle is at (250, 250). 40 is the radius. (0, 0, 255) is the color (red).
# 'thickness' is the border thickness.
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=3)
cv.imshow('Circle', blank)

# Draw a line
# (0, 0) is the starting point, (250, 250) is the endpoint of the line.
# (255, 0, 255) is the color (magenta). 'thickness' is the thickness of the line.
cv.line(blank, (0, 0), (250, 250), (255, 0, 255), thickness=4)
cv.imshow('Line', blank)





#Writing text on the Image


#Here blank is the image.Then we have to write the text which we want to display.(0,255) is the x,y axis. Then we decided the font . 1.0 is the font-scale.(0,255,255) is the color.


cv.putText(blank,'Hello I am a Box',(0,255),cv.FONT_HERSHEY_TRIPLEX,
           1.0,(0,255,255),thickness=2)

cv.imshow('Text-image',blank)


cv.waitKey(0)
