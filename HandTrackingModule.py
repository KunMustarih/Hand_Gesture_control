import cv2
import mediapipe as mp
import time


# class creation
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, modelComplexity=1, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity 
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils  # it gives small dots onhands total 20 landmark points

    def findHands(self, img, draw=True):
        # Send rgb image to hands
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)  # process the frame
        #     print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    # Draw dots and connect them
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0, draw=True):
        """Lists the position/type of landmarks
        we give in the list and in the list ww have stored
        type and position of the landmarks.
        List has all the lm position"""

        lmlist = []

        # check wether any landmark was detected
        if self.results.multi_hand_landmarks:
            # Which hand are we talking about
            myHand = self.results.multi_hand_landmarks[handNo]
            # Get id number and landmark information
            for id, lm in enumerate(myHand.landmark):
                # id will give id of landmark in exact index number
                # height width and channel
                h, w, c = img.shape
                # find the position
                cx, cy = int(lm.x * w), int(lm.y * h)  # center
                # print(id,cx,cy)
                lmlist.append([id, cx, cy])

                # Draw circle for 0th landmark
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        return lmlist

    def fingersUp(self,lmList):
        fingertips = [4, 8, 12, 16, 20]
        Open_fingers = []
        if len(lmList) != 0:

            #Thumb
            if lmList[fingertips[0]][1] < lmList[fingertips[0] - 1][1]:
                Open_fingers.append(1)
            else:
                Open_fingers.append(0)


            for tip in range(1,5):
                if lmList[fingertips[tip]][2] < lmList[fingertips[tip] -2][2]:
                    Open_fingers.append(1)
                else:
                    Open_fingers.append(0)

            return Open_fingers
def main():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        detector.fingersUp(lmList)

        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
