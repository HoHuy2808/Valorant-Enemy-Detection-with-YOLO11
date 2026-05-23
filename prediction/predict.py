from ultralytics import YOLO
import cv2

model = YOLO("./prediction/best.pt")

cap = cv2.VideoCapture("./video/VOD.mp4")

current_frame = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break


    results = model(frame)

    annotated = results[0].plot()

    cv2.imshow("Detection", annotated)
    
    current_frame += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()