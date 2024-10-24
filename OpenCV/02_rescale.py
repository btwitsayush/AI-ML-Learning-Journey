import cv2 as cv


img=cv.imread("C:\\Users\\Admin\\Downloads\\th.jpg")
cv.imshow('Box',img)


#This function will work from images,videos,live webcam as well

def rescaleFrame(frame,scale=0.75):  #scale0.75 means it will convert our frame to 75% from 100%

    width=int(frame.shape[1]*scale) #frame.shape[1] refers to width of frame
    height=int(frame.shape[0]*scale)#frame.shape[0] refers to width of frame
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


capture=cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)#calling the function to resize the frame
    image_resized=rescaleFrame(img)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    cv.imshow('Resized-img',image_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

