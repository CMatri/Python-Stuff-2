import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width = 640
height = 480
r_range = np.arange(-4, 4, 8 / width)
i_range = np.arange(-4, 4, 8 / height)

def f(xr, xi):
    return xr * xr - xi * xi, 2 * xr * xi

while True:
    ret, frame = cap.read()
    conformed = np.ndarray(frame.shape)

    for y, row in enumerate(frame):
        for x, pixel in enumerate(row):
            cx, cy = f(r_range[x], i_range[y])
            cx *= 8
            cy *= 8
            cx = min(width - 1, cx)
            cy = min(height - 1, cy)
            conformed[y][x] = frame[int(cy)][int(cx)]

    cv2.imshow('orig', frame)
    cv2.imshow('mapping', conformed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
