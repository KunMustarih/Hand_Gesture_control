import math
import cv2
import numpy as np
import HandTrackingModule as htm
import vlc
import time
import pyautogui

media_player = vlc.MediaPlayer()
media = vlc.Media("Thor.mp4")
media_player.set_media(media)
minVolume = 0
maxVolume = 100

WCAM, HCAM = 640, 480
state = "play"
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# media_player.play()
cap.set(3, WCAM)
cap.set(4, HCAM)

detector = htm.handDetector(detectionCon=0.7)
pyautogui.getWindowsWithTitle("vlc")[0].activate()
pyautogui.press('space')


def control_volume(length):
    volume = np.interp(length, [20, 145], [minVolume, maxVolume])
    media_player.audio_set_volume(int(volume))


def pause_video():
    pyautogui.getWindowsWithTitle("vlc")[0].activate()
    pyautogui.press('space')


def play_video():
    pyautogui.getWindowsWithTitle("vlc")[0].activate()
    pyautogui.press('space')


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) != 0:
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        length = math.hypot(x2 - x1, y2 - y1)
        control_volume(length)

        a = detector.fingersUp(lmlist)

        if a == [0, 1, 0, 0, 0] and state == "play":
            pause_video()
            state = "pause"
            print("d")

        if a == [0, 1, 1, 0, 0] and state == "pause":
            play_video()
            state = "play"

    cv2.imshow("Video", img)
    cv2.waitKey(1)
