import cv2
import mediapipe as mp
import time
from modules import pose_module as pm




cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img , results= detector.findPose(img)
    lmList = detector.findPosition(img,results)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()