#Face blur script

import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 5)

for (x, y, w, h) in faces:
    face_roi = frame[y:y+h, x:x+w]
    face_roi = cv2.GaussianBlur(face_roi, (99, 99), 30)
    frame[y:y+h, x:x+w] = face_roi
    cv2.imshow("Live Face Blur", frame)
    
    #press q to stop
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cap.release()
    cv2.destroyAllWindows()
