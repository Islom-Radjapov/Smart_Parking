import cv2
from sql_code import get_stiuation

camera = cv2.VideoCapture("test_media/qora.MOV")
font = cv2.FONT_HERSHEY_SIMPLEX


while True:
    ret, frame = camera.read()

    cv2.putText(frame, f"{get_stiuation()} Raqamli joy bo'sh!", (50, 450), font, 1, (255, 0, 0), 2)

    cv2.imshow('canny',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()