import cv2
import time

#IP Camera Information
scheme = '192.168.1.'
stream = 'live'
host = scheme + '55'

#capture = cv2.VideoCapture('rtsp://' + host + ':554/' + stream)
capture = cv2.VideoCapture('rtsp://192.168.1.55:554/' + stream)

while True:
    _, frame = capture.read()

    #Place options to overlay on the video hereself.
    #I'll go over that later

    cv2.imshow(('Camera' + str(1)), frame)

    #time.sleep(5)

    k = cv2.waitKey(0) & 0xFF
    if k == 27: #esc key ends process
        capture.release()
        break
cv2.destroyAllWindows()
