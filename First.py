import cv2 as cv

# 1) Reading Image and Video

# Reading Image
# img = cv.imread("/home/majid/Pictures/OpenCV/Zeeshan.jpg")
# cv.imshow("Image", img)
# cv.waitKey(0)


# Reading Video

# capture = cv.VideoCapture("/home/majid/Pictures/OpenCV/Song.mp4")
#
# while True:
#     isTrue, frame= capture.read()
#     cv.imshow("Video", frame)
#
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()


# 2) Resizing and Rescaling


# img=cv.imread("/home/majid/Pictures/OpenCV/mn.jpg")
# die=img.shape
# print(die)
# cv.imshow("Image",img)
# cv.waitKey(0)

# I) Rescaling

# img = cv.imread("/home/majid/Pictures/OpenCV/Zeeshan.jpg")
# cv.imshow("Image", img)
#
# def rescaleFrame(frame, scale=0.75):
#     # this function is work images, videos and live videos
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#
#     diemensions = (width, height)
#
#     return cv.resize(frame, diemensions, interpolation=cv.INTER_AREA)
#
#
# # change Resolution of Live Video
# # def ChangeRes(width, height):
# #     capture.set(3,width)
# #     capture.set(4,height)
#
# # Reading Video
#
# resized_img=rescaleFrame(img,scale=0.5)
# cv.imshow("Image2", resized_img)
#
# capture = cv.VideoCapture("/home/majid/Pictures/OpenCV/Song.mp4")
#
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame, scale=0.2)
#
#     cv.imshow("Video", frame)
#     cv.imshow("Resized Video", frame_resized)
#
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()





