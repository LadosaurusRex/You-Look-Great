import cv2
from picamera2 import Picamera2
import face_recognition
import time


face_locations = []

frame_count = 0

#set the number of frames ignored before running the facial detection
frame_rate = 1


picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (640, 360), "format": "BGR888"}, encode="main") #1280, 720
picam2.configure(config)
picam2.start()


time.sleep(0.1)



while True:
    time.sleep(1)
    # Grab a single frame of video
    frame = picam2.capture_array("main")

    #count the number of frames captured
    frame_count = frame_count + 1

    #only process a frame every frame_rate number of frames
    if frame_count > frame_rate:

        #Reset the frame_count to zero
        frame_count = 0

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces in the current frame of video
        # face_locations = face_recognition.face_locations(rgb_frame)

        # Display the results
        # for top, right, bottom, left in face_locations:
        #    # Draw a box around the face
        #    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Display the resulting image
        cv2.imshow('Video', frame)
        

    # Wait for Enter key to stop
    if cv2.waitKey(25) == 13:
        break

# Release everything if job is finished
cv2.destroyAllWindows()
