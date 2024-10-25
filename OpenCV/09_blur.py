import cv2 as cv

# Load an image from the specified file path

img = cv.imread("C:\\Users\\Admin\\Downloads\\th.jpg")


cv.imshow('Box', img)

# ---- Averaging Blur ----
# This method smooths the image by taking the average of pixel values in a small region (kernel).
# The kernel size here is 7x7, meaning it averages the colors of 7x7 pixels.
# A larger kernel size will make the image blurrier.
average = cv.blur(img, (7, 7))


cv.imshow('Average-Blur', average)

# ---- Gaussian Blur ----
# Gaussian blur uses a weighted average, where central pixels are given more importance.
# The kernel size is still 7x7, and the third parameter (0) automatically calculates the sigma value.
# This blur is smoother and less harsh than the average blur.
gauss = cv.GaussianBlur(img, (7, 7), 0)


cv.imshow('Gaussian-Blur', gauss)

# ---- Median Blur ----
# Median blur replaces each pixel's value with the median of its surrounding pixels.
# It's good at removing noise while keeping edges sharp.
# The kernel size must be an odd number, here it's set to 7.
median = cv.medianBlur(img, 7)


cv.imshow('Median-Blur', median)

# ---- Bilateral Blur ----
# Bilateral blur keeps edges sharp while smoothing the rest.
# The first parameter (5) is the diameter of the pixel neighborhood.
# The second (15) is the sigma value for color, affecting how colors are blurred.
# The third (15) is the sigma value for space, affecting how far pixels influence each other.
bilateral = cv.bilateralFilter(img, 5, 15, 15)


cv.imshow('Bilateral-Blur', bilateral)

# Wait for a key press indefinitely before closing the windows
cv.waitKey(0)
