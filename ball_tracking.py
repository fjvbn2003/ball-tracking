# USAGE
# python ball_tracking.py --video ball_tracking_example.mp4
# python ball_tracking.py

# import the necessary packages

import cv2
import time
# construct the argument parse and parse the arguments

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (30, 100, 100)
greenUpper = (90, 255, 255)

vs = cv2.VideoCapture(0)
time.sleep(2)

# if a video path was not supplied, grab the reference
# to the webcam

# otherwise, grab a reference to the video file

# keep looping
while True:
	# grab the current frame
    if(vs.isOpened()):    
        t_ok , frame= vs.read()

	# handle the frame from VideoCapture or VideoStream

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video

	# resize the frame, blur it, and convert it to the HSV
	# color space
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
    image, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    center = None

	# only proceed if at least one contour was found
    if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if the radius meets a minimum size
        if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

	# update the points queue
	# show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
vs.release()
cv2.destroyAllWindows()


# close all windows
cv2.destroyAllWindows()