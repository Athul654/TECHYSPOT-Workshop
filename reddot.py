import cv2
import mediapipe as mp

mp_face=mp.solutions.face_detection
mp_drawing=mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)
with mp_face.FaceDetection(model_selection=0,min_detection_confidence=0.5) as face_detection:
 while True:
    ret,frame=cap.read()
    if not ret:
        break
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=face_detection.process(rgb_frame)

    if results.detections:
        h, w, c = frame.shape 
        for detection in results.detections:
            box = detection.location_data.relative_bounding_box
            x = int(box.xmin * w)
            y = int(box.ymin * h)
            bw = int(box.width * w)
            bh = int(box.height * h)

            fx = x + bw // 2
            fy = y + int(bh * 0.15)
            cv2.circle(frame, (fx, fy), 5, (0, 0, 255), -1)

    cv2.imshow("camera",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break 
cap.release()
cv2.destroyAllWindows()