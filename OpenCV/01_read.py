import cv2 as cv




#to read images

img=cv.imread("C:\\Users\\Admin\\Downloads\\th.jpg")

#it is used to open the image
cv.imshow('Box',img)

#waitKey will tell for how much milliseconds image will be opend. 0 means infinite
cv.waitKey(0)

#to read videos

#to read specific video we provide the path
#to read the live video from webcam we use 0


capture=cv.VideoCapture(0)

while True:
    isTrue,frame=capture.read()  #it is capturing each and every frame of our video
    cv.imshow('Video',frame) #it will show the video frame by frame


#cv.waitKey(20) will wait for 20 milliseconds between each frame. This means the loop pauses for 20ms while processing each frame, which allows the video to play smoothly.
#to stop reading live video we need to press 'd'.
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break



capture.release() #it will release the camera
cv.destroyAllWindows()#close all the opencv windows


