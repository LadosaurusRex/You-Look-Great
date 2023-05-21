#import cv2
import face_recognition
import sys
import time
from picamera2 import Picamera2, Preview

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)


picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (640, 360), "format": "BGR888"}, encode="main") #1280, 720
picam2.configure(config)
picam2.start()

# video_capture = cv2.VideoCapture(0)

face_locations = []

face_detected = "Non"

sign_on = 0

frame_count = 0

no_face_count = 0

#set the number of frames ignored before running the facial detection
frame_rate = 5

GPIO.output(4,GPIO.LOW)

while True:
    time.sleep(1)


    # Grab a single frame of video
    # ret, frame = video_capture.read()

    #count the number of frames captured
    #frame_count = frame_count + 1

    #only process a frame every frame_rate number of frames
    #if frame_count > frame_rate:

        #Reset the frame_count to zero
        #frame_count = 0

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = picam2.capture_array("main")

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    #Turn the output into boolean
    if len(face_locations) > 0:
        face_detected = "Yes"

        time.sleep(1)

        sign_on = 1
        print(time.strftime('%H:%M:%S',time.localtime()),"sign_on? =  " + str(sign_on))
        
        GPIO.output(4,GPIO.HIGH)

    else:
        face_detected = "Non"
        no_face_count = no_face_count + 1
        if no_face_count > 5:
            sign_on = 0
            print(time.strftime('%H:%M:%S',time.localtime()),"sign_on? =  " + str(sign_on))
            no_face_count = 0
            
            GPIO.output(4,GPIO.LOW)


    # Display via text if there is a face detected ,,
    #        print("Faces Detected? =  " + str(face_detected), end='\r',)
    # print(time.strftime('%H:%M:%S',time.localtime()),"sign_on? =  " + str(sign_on))


    # Wait for Enter key to stop
    # if cv2.waitKey(25) == 13:
    #    break

