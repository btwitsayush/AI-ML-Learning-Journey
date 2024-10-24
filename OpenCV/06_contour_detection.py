import cv2 as cv



img=cv.imread("C:\\Users\\Admin\\Downloads\\th.jpg")

cv.imshow('Box',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey-img',gray)

canny=cv.Canny(img,125,175)
cv.imshow('Canny-img',canny)



contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

#To find the contours we also have 1 more method which is threshold 


 
cv.waitKey(0)