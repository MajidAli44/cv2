import cv2 as cv
import numpy as np

blank = np.zeros((480, 480, 3), dtype="uint8")
cv.imshow("Blank", blank)

# paint the image with Certain color

# blank[200:300, 250:350] = 0,255,0
# cv.imshow("Color Image", blank)

# Draw a Rectangle

# cv.rectangle(blank,(0,0),(240,480),(0,255,255),thickness=-1)
# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 255), thickness=-1)
# cv.imshow("Rectangle", blank)
#
#
# # Draw Circle
#
# cv.circle(blank, (240,240), 80, (0, 255, 0), thickness=-1)
# cv.imshow("Circle", blank)
#
# # Draw Line
#
#
# cv.line(blank,(0,0),(240,240),(155,255,255),thickness=4)
# cv.imshow("Line", blank)

# Write Text
cv.putText(blank,("Majid Ali"),(150,240),cv.FONT_HERSHEY_TRIPLEX,1.2,(0,255,0),thickness=5)
cv.imshow("Text Image", blank)


cv.waitKey(0)