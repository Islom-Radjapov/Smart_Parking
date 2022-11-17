import cv2
import csv


class spots:
    loc = 0

def drawRectangle(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    pix = cv2.countNonZero(edges)
    if pix in range(min, max):
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)
        spots.loc += 1
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)


def callback(foo):
    pass


with open('car_data/rois.csv', 'r', newline='') as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)
rois = [[int(float(j)) for j in i] for i in rois]

cv2.namedWindow('parameters')
cv2.createTrackbar('Threshold1', 'parameters', 186, 700, callback)
cv2.createTrackbar('Threshold2', 'parameters', 122, 700, callback)
cv2.createTrackbar('Min pixels', 'parameters', 100, 1500, callback)
cv2.createTrackbar('Max pixels', 'parameters', 323, 1500, callback)

VIDEO_SOURCE = 0
cap = cv2.VideoCapture(VIDEO_SOURCE)

# start the live feed
while True:
    # set the number of spots to 0
    spots.loc = 0

    # set two frames for the feed
    ret, frame = cap.read()
    ret2, frame2 = cap.read()

    # define the range of pixels and the thresholds for Canny function
    min = cv2.getTrackbarPos('Min pixels', 'parameters')
    max = cv2.getTrackbarPos('Max pixels', 'parameters')
    lowThreshold = cv2.getTrackbarPos('Threshold1', 'parameters')
    highThreshold = cv2.getTrackbarPos('Threshold2', 'parameters')

    # apply the function for every list of coordinates
    for i in range(len(rois)):
        drawRectangle(frame, rois[i][0], rois[i][1], rois[i][2], rois[i][3])

    # adding the number of available spots on the shown image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Available spots: ' + str(spots.loc), (10, 30), font, 1, (0, 255, 0), 3)
    cv2.imshow('frame', frame)

    # displaying the image with Canny function applied for reference
    canny = cv2.Canny(frame2, lowThreshold, highThreshold)
    cv2.imshow('canny', canny)

    # listen for 'Q' key to stop the stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()