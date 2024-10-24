import cv2 as cv
import numpy as np

# Load an image from a file
img = cv.imread("C:\\Users\\Admin\\Downloads\\th.jpg")

# Display the original image in a window named 'Box'
cv.imshow('Box', img)

# Translation function - shifts the image left/right and up/down
def translate(img, x, y):
    # Create a translation matrix to move the image. 
    # The matrix format is [[1, 0, x], [0, 1, y]] where x and y are the translation values.
    transMatrix = np.float32([[1, 0, x], [0, 1, y]])

    # Get the dimensions of the image (width, height) to use when translating.
    dimensions = (img.shape[1], img.shape[0])

    # Apply the translation to the image using the translation matrix and the image dimensions.
    # cv.warpAffine changes the position of the image based on the translation matrix.
    return cv.warpAffine(img, transMatrix, dimensions)

# How to interpret the translation values:
# -x ---> Shift left
# -y ---> Shift up
#  x ---> Shift right
#  y ---> Shift down

# Translate the image 100 pixels to the left and 100 pixels up
translated = translate(img, -100, -100)

# Display the translated image in a window named 'Translated-Image'
cv.imshow('Translated-Image', translated)

# Wait for a key press to close the windows


#Rotation

# Function to rotate the image
def rotate(img, angle, rotPoint=None):
    # Get the height and width of the image
    (height, width) = img.shape[:2]

    # If no rotation point is given, use the center of the image
    if rotPoint is None:
        # // is integer division, dividing width and height by 2 to get the center point
        rotPoint = (width // 2, height // 2)

    # Create the rotation matrix with the rotation point, angle, and scale factor (1.0 keeps the size the same)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    # Set the dimensions for the output image (same width and height as the original)
    dimensions = (width, height)

    # Apply the rotation to the image using the rotation matrix
    return cv.warpAffine(img, rotMat, dimensions)

# Rotate the image by -45 degrees (counter-clockwise)
rotated = rotate(img, 45)


cv.imshow('Rotated-Image', rotated)



# Flip the image
# cv.flip(img, flipCode) is used to flip the image. 
# The 'flipCode' decides how to flip the image:
# 0 --> Flips the image vertically (upside down)
# 1 --> Flips the image horizontally (left to right)
# -1 --> Flips the image both vertically and horizontally (upside down and reversed)
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)



cv.waitKey(0)