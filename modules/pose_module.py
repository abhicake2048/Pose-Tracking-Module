import cv2
import mediapipe as mp
import time


class poseDetector():
    def __init__(self, mode =False , upBody=False, smooth=True,detectionCon = 0.7, trackCon = 0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon >= 0.5
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,self.detectionCon,self.trackCon)

    def findPose(self,img,draw = True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)

        if results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        return img,results
    
    def findPosition(self,img,results,draw = True):
        lmList = []
        if results.pose_landmarks:
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w) , int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),2,(0,255,0),cv2.FILLED)
        return lmList



def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img,results = detector.findPose(img)
        lmList = detector.findPosition(img,results)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)



        cv2.imshow("image",img)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()