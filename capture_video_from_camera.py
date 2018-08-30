import numpy 
import cv2

cap = cv2.VideoCapture(0) # It requires to create a object for each camera
# It possible change the variable into a IP address that you want to connect

cap.set(3, 640)
cap.set(4, 480)

while(True):
    ret, frame = cap.read() # Capture frame by frame 
    # img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # img = cv2.IMREAD_UNCHANGED
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
