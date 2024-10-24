import cv2 as cv

# Load an image from a file
img = cv.imread("C:\\Users\\Admin\\Downloads\\th.jpg")
cv.imshow('Box-Image', img)

# Convert the image to grayscale
# This changes the image from color (RGB) to grayscale, which has only shades of gray.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray-Image', gray)

# Blur the image
# Uses Gaussian Blur to soften the image. (5,5) is the kernel size, which controls the amount of blur.
# cv.BORDER_DEFAULT is the border type used for padding the image edges.
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blurred-Image', blur)

# Edge detection using Canny edge detection
# Detects edges in an image by identifying areas of rapid intensity change. 
# The two values (125, 175) are the lower and upper threshold values for edge detection.
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny-Image', canny)

# Dilating the image
# Makes the white regions in the image thicker (edges become bolder) by expanding them.
# (3,3) is the kernel size (the area considered for dilation), and 'iterations' determines how many times to apply the dilation.
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('Dilated-Image', dilated)

# Eroding the image
# Makes the white regions thinner by eroding away pixels. This is useful to remove small noise.
# (3,3) is the kernel size, and 'iterations' is the number of times erosion is applied.
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded-Image', eroded)

# Resize the image
# Resizes the image to 500x500 pixels.
resized = cv.resize(img, (500, 500))
cv.imshow('Resized-Image', resized)

# Cropping the image
# Crops the image using array slicing. The format is img[y1:y2, x1:x2].
cropped = img[100:200, 200:400]
cv.imshow('Cropped-Image', cropped)

# Wait for a key press to close the windows
cv.waitKey(0)
