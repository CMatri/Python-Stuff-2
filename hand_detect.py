import numpy as np
from numpy import sqrt,arccos,rad2deg
import cv2

cap = cv2.VideoCapture(0)

#cv2.namedWindow("img1",cv2.WINDOW_NORMAL)
#cv2.namedWindow("img2",cv2.WINDOW_NORMAL)
#cv2.namedWindow("img3",cv2.WINDOW_NORMAL)
#cv2.namedWindow("img4",cv2.WINDOW_NORMAL)
#cv2.namedWindow("img5",cv2.WINDOW_NORMAL)
cv2.namedWindow("img6",cv2.WINDOW_NORMAL)
#cv2.namedWindow("Finger tracking",cv2.WINDOW_NORMAL)

def triple_channel(frame):
    return  np.repeat(frame[:, :, np.newaxis], 3, axis=2)

while(True):
    ret, frame = cap.read()
    image = cv2.flip(frame, 1)
    #cv2.imshow("img1", image)

    original_img = image.copy()
    no_filter_img = image.copy()

    image = cv2.blur(image, (5, 5))
    #cv2.imshow('img2', image)

    MIN = np.array([0, 30, 60], np.uint8)
    MAX = np.array([20, 150, 179], np.uint8)
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #cv2.imshow("img3", hsv_img)

    filter_img = cv2.inRange(hsv_img, MIN, MAX)
    #cv2.imshow("img4", filter_img)

    filterImg = cv2.erode(filter_img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
    #cv2.imshow("img5",filterImg)

    filterImg = cv2.dilate(filter_img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
    cv2.imshow("img6",filterImg)

    """
    img_a, contours, heirarchy = cv2.findContours(filterImg,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)


    if not len(contours): continue

    index = []
    index_val = 0

    for cnt in contours:
        temp_img = image.copy()
        temp_img = cv2.subtract(temp_img, image)
        hull = cv2.convexHull(cnt)
        last = None

        for h in hull:
            if last == None:
                cv2.circle(temp_img, tuple(h[0]), 5, (0, 255, 255), 2)
            else:
                x = abs(last[0] - tuple(h[0])[0])
                y = abs(last[1] - tuple(h[0])[1])
                distance = sqrt(x**2 + y**2)
                if distance > 10:
                    cv2.circle(temp_img, tuple(h[0]), 5, (0, 255, 255), 2)
            last = tuple(h[0])

        m = cv2.moments(cnt)

        if(m["m00"] == 0): continue

        c_x = int(m["m10"] / m["m00"])
        c_y = int(m["m01"] / m["m00"])
        cv2.circle(temp_img, (c_x, c_y), 10, (255, 255, 0), 2)
        hull = cv2.convexHull(cnt, returnPoints=False)
        defects = cv2.convexityDefects(cnt, hull)

        if defects is None: continue

        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]

            if d > 1000:
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])

                cv2.circle(temp_img, far, 5, (255, 255, 255), -2)
                cv2.line(temp_img, start, far, (0, 255, 0), 5)
                cv2.line(temp_img, far, end, (0, 255, 0), 5)

        #original_img = cv2.add(original_img, temp_img)
        index_val += 1

    cv2.drawContours(original_img, contours, -1, (255, 0, 0), -2)
    cv2.imshow("Finger tracking", original_img)
    """

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
