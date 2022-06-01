import cv2
import HandTrackingModule as htm
import pyautogui


WCAM, HCAM = 640, 480
state = "play"
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(3, WCAM)
cap.set(4, HCAM)

detector = htm.handDetector(detectionCon=0.7)
pyautogui.getWindowsWithTitle("vlc")[0].activate()
pyautogui.press('space')

def pause_video():
    pyautogui.press('space')

def play_video():
    pyautogui.press('space')

def Volume_Up():
    pyautogui.press('volumeup')

def Volume_down():
    pyautogui.press('volumedown')



while True:
    success, img = cap.read()
    img = detector.findHands(img)
    img = cv2.flip(img, 1)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) != 0:
        a = detector.fingersUp(lmlist)

        if a == [0, 0, 0, 0, 0] and state == "play":
            pause_video()
            state = "pause"

        if a == [1, 1, 1, 1, 1] and state == "pause":
            play_video()
            state = "play"

        if a == [0,1,1,1,0]:
            Volume_down()

        if a == [0,1,1,1,1]:
            Volume_Up()


    cv2.imshow("Video", img)
    cv2.waitKey(1)
