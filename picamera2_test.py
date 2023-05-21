from picamera2 import Picamera2, Preview
import time
picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (1280, 720), "format": "BGR888"}, encode="main")
picam2.configure(config)
picam2.start()
time.sleep(2)
array = picam2.capture_array("main")
print(array.shape)
