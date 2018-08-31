import numpy 
import cv2
from datetime import datetime as dt

cap = cv2.VideoCapture(0) # It requires to create a object for each camera
cap2 = cv2.VideoCapture(1) # It requires to create a object for each camera
# It possible change the variable into a IP address that you want to connect

date_now = str(dt.now().strftime("%c"))  

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videos/' + date_now + '.avi', fourcc, 5.0, (640,480))
out2 = cv2.VideoWriter('videos/' + date_now + '2.avi', fourcc, 5.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read() # Capture frame by frame 
    ret2, frame2 = cap2.read() # Capture frame by frame 
    # img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # img = cv2.IMREAD_UNCHANGED

    if ret == True:
        #frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow('frame', frame)

        out.write(frame2)
        cv2.imshow('frame', frame2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
