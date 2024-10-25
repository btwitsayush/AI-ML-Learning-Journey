import cv2 as cv
import matplotlib.pyplot as plt


img=cv.imread("C:\\Users\\Admin\\Downloads\\th.jpg")

cv.imshow('Box',img)

"""
If we use any other library other than open cv it will read out file in RGB mode

plt.imshow(img)
plt.show()
"""


#BGR To GrayScale

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grey-Image",gray)


#BGR To HSV (Hue Saturation Veiw)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV-Image',hsv)

#BGR To LAB

lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB-Image',lab)

# BGR To RGB

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB-Image',rgb)


cv.waitKey(0)
