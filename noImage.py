import cv2
import face_recognition
import sys

video_capture = cv2.VideoCapture(0)

face_locations = []

face_detected = "Non"

frame_count = 0

#set the number of frames ignored before running the facial detection
frame_rate = 5


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    #count the number of frames captured
    frame_count = frame_count + 1

    #only process a frame every frame_rate number of frames
    if frame_count > frame_rate:

        #Reset the frame_count to zero
        frame_count = 0

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)

        #Turn the output into boolean
        if len(face_locations) > 0:
            face_detected = "Yes"
        else:
            face_detected = "Non"


        # Display via text if there is a face detected ,,
        print("Faces Detected? =  " + str(face_detected), end='\r',)



        # Wait for Enter key to stop
        if cv2.waitKey(25) == 13:
            break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
