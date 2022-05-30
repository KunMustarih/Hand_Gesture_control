import math
import cv2
import numpy as np
import HandTrackingModule as htm
import vlc
import time

# media_player= vlc.MediaPlayer()
# media = vlc.Media("Thor.mp4")
#
# media_player.set_media(media)
#
# media_player.play()
# time.sleep(10)

WCAM, HCAM = 640,480


cap = cv2.VideoCapture(0)
cap.set(3,WCAM)
cap.set(4,HCAM)


detector = htm.handDetector(detectionCon=0.7)






while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img,draw=False)
    if len(lmlist) != 0:
       #145 and 10

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]

        cx,cy = (x1+x2) // 2, (y1+y2) // 2

        cv2.circle(img,(x1,y1),10,(255,0,255),cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)


        length = math.hypot(x2-x1,y2-y1)
        if length < 12:
           cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
        print(length)



    cv2.imshow("Video",img)
    cv2.waitKey(1)