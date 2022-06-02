import pyautogui
import win32gui
import cv2
import HandTrackingModule as htm

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        x = str(win32gui.GetWindowText( hwnd ))
        if "PowerPoint" in x:
            pyautogui.getWindowsWithTitle(x)[0].maximize()
win32gui.EnumWindows( winEnumHandler, None )


WCAM, HCAM = 640, 480
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
with pyautogui.hold('fn'):
    pyautogui.press(['f5'])

cap.set(3, WCAM)
cap.set(4, HCAM)

detector = htm.handDetector(detectionCon=0.7)




while True:
    success, img = cap.read()
    img = detector.findHands(img)
    img = cv2.flip(img, 1)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) != 0:
        a = detector.fingersUp(lmlist)


        # if a == [0, 1, 1, 1, 0]:
        #     Volume_down()
        #
        # if a == [0, 1, 1, 1, 1]:
        #     Volume_Up()
        #
        # if a == [0, 1, 0, 0, 0]:
        #     move_backward()
        #
        # if a == [0, 1, 1, 0, 0]:
        #     move_forward()

    cv2.imshow("Video", img)
    cv2.waitKey(1)
