#basic security camera
#grab a free account from twilio.com

import cv2
import time
from twilio.rest import Client

# Twilio your credentials
TWILIO_SID = 'enter your twilio sid here'
TWILIO_AUTH_TOKEN = 'enter your auth token here'
FROM_PHONE = 'your twilio phone number'
TO_PHONE = 'your phone number'
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_sms():
    try:
        message = client.messages.create(
            body="[!] MOTION DETECTED [!]",
            from_=FROM_PHONE,
            to=TO_PHONE
        )
        print(f"[SMS SENT] SID: {message.sid}")
    except Exception as e:
        print(f"[ERROR SENDING SMS]: {e}")

video = cv2.VideoCapture(0)
time.sleep(2)

first_frame = None
motion_detected = False
motion_timer = 0

while True:
    check, frame = video.read()
    if not check:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_in_frame = False
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        motion_in_frame = True
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Check enougg time
    if motion_in_frame:
        if not motion_detected or time.time() - motion_timer > 60:
            send_sms()
            motion_detected = True
            motion_timer = time.time()
        status_text = "Motion Detected"
    else:
        status_text = "No Motion"

    cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Motion Detector", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

if key == ord('q'):
    break
video.release()
cv2.destroyAllWindows()
