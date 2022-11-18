import cv2
import easyocr

plateCascade = cv2.CascadeClassifier("ML_models\model.xml")

camera = cv2.VideoCapture("test_videos/test.mp4")
minArea = 500
count = 0

while camera.isOpened():
    ret, frame = camera.read()
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "NumberPlate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            imgRoi = frame[y:y + h, x: x + w]
        # rasmdan nomerni oqib olish
        reader = easyocr.Reader(['en'])
        result = reader.readtext(imgRoi)
        iff = bool(result)
        if iff:
            # faqat nomerni olish
            print(result[1][1])

    cv2.imshow("Result", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
    ...