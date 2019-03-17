import cv2
import time
vs = cv2.VideoCapture(0)
time.sleep(2)

# if a video path was not supplied, grab the reference
# to the webcam

# otherwise, grab a reference to the video file
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')
# keep looping
while True:
	# grab the current frame
    left_ok , img = vs.read()
    if(vs.isOpened()):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
        cv2.imshow("output", img)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
vs.release()
cv2.destroyAllWindows()