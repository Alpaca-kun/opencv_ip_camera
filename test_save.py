import numpy 
import cv2
from datetime import datetime as dt

cap = cv2.VideoCapture(0) # It requires to create a object for each camera
# It possible change the variable into a IP address that you want to connect

date_now = str(dt.now().strftime("%c"))  

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videos/' + date_now + '.avi', fourcc, 20.0, (640,480))

count = 0
while(cap.isOpened()):
    ret, frame = cap.read() # Capture frame by frame 
    # img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # img = cv2.IMREAD_UNCHANGED

    if ret == True:
        #frame = cv2.flip(frame, 0)
        out.write(frame)
        
        count += 1
        print(count)

        if count == 300:
            cap.release()
            break
    
    
    else:
        cap.release()
        break

out.release()
cv2.destroyAllWindows()
