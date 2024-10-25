import cv2 as cv
import numpy as np


img=cv.imread("C:\\Users\\Admin\\Downloads\\th.jpg")

cv.imshow('Box',img)

#blank image


#spliting the image in different colors
b,g,r=cv.split(img)
blank=np.zeros(img.shape[:2],dtype='uint8')


#image is consist of 3 components 
#b,g,r in this order
blue=cv.merge([b,blank,blank])#here we are showing blue color of image and for g,r it will be blank
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])


cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merging all the split colors
merged=cv.merge([b,g,r])
cv.imshow('Merged-Image',merged)

cv.waitKey(0)