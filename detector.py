from time import sleep
import cv2
import csv
from sql_code import add_stiuation, get_all

font = cv2.FONT_HERSHEY_SIMPLEX
def drawRectangle(img, a, b, c, d, num):
    sub_img = img[b:b + d, a:a + c]
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    pix = cv2.countNonZero(edges)
    if pix in range(min, max):
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)
        cv2.putText(img, f"{num}", (a, b), font, 1, (0, 255, 0), 2)
        add_stiuation(num, 0)
    else:
        add_stiuation(num, 1)
        cv2.putText(img, f"{num}", (a, b), font, 1, (0, 255, 0), 2)
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)

def callback(foo):
    pass

with open('coordinates/rois.csv', 'r', newline='') as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)
rois = [[int(float(j)) for j in i] for i in rois]

cv2.namedWindow('parameters')
cv2.createTrackbar('Threshold1', 'parameters', 545, 700, callback)
cv2.createTrackbar('Threshold2', 'parameters', 402, 700, callback)
cv2.createTrackbar('Min pixels', 'parameters', 100, 1500, callback)
cv2.createTrackbar('Max pixels', 'parameters', 323, 1500, callback)


camera = cv2.VideoCapture("test_videos/bay-park-2.gif")

# start the live feed
while camera.isOpened():


    ret, frame = camera.read()
    ret2, frame2 = camera.read()

    min = cv2.getTrackbarPos('Min pixels', 'parameters')
    max = cv2.getTrackbarPos('Max pixels', 'parameters')
    lowThreshold = cv2.getTrackbarPos('Threshold1', 'parameters')
    highThreshold = cv2.getTrackbarPos('Threshold2', 'parameters')


    for i in range(len(rois)):
        drawRectangle(frame, rois[i][0], rois[i][1], rois[i][2], rois[i][3], i)
        cv2.putText(frame, f"Barcha band joylar=> {get_all()[0]}", (40, 450), font, 1, (0, 0, 255), 2)
        cv2.putText(frame, f"Bosh joylar=> {get_all()[1]}", (500, 450), font, 1,(255, 0, 0), 2)


    cv2.imshow('frame', frame)
    sleep(0.15)

    # chorniy holatida ham korsatadi
    # canny = cv2.Canny(frame2, lowThreshold, highThreshold)
    # cv2.imshow('canny',canny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
    ...

