import cv2 as cv
import numpy as np

# Create a blank black image of size 400x400 with a single color channel (grayscale)
# 'uint8' is the data type, meaning the pixel values range from 0 to 255
blank = np.zeros((400, 400), dtype='uint8')

# Create a white rectangle on a black background
# Top-left corner at (30, 30), bottom-right corner at (370, 370), color 255 (white), and fill it completely (-1)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

# Create a white circle on a black background
# Centered at (200, 200), with a radius of 200, color 255 (white), and fill it completely (-1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

# Display the rectangle and circle images
cv.imshow("Rectangle-Image", rectangle)
cv.imshow("Circle-Image", circle)

# ---- Bitwise Operations ----

# Bitwise-AND -> Intersection of rectangle and circle
# Only the overlapping (intersection) area of the rectangle and circle will remain white
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise-AND Image", bitwise_and)

# Bitwise-OR -> Union of rectangle and circle
# Both the intersection and the non-intersection areas of rectangle and circle will be white
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise-OR Image", bitwise_or)

# Bitwise-XOR -> Non-intersecting areas of rectangle and circle
# Only the non-overlapping areas will remain white
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise-XOR Image", bitwise_xor)

# Bitwise-NOT -> Invert colors of the image
# White becomes black, and black becomes white
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise-NOT Image", bitwise_not)

# Wait for a key press indefinitely before closing the windows
cv.waitKey(0)
