import cv2

image = cv2.imread("D:\PICTURES\ttu.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = 255 - gray_image
blur = cv2.GaussianBlur(inverted, (21, 21), 0)
invertedblur = 255 - blur
sketch = cv2.divide(gray_image, invertedblur, scale=256.0)
cv2.imwrite("Sketch.png", sketch)
cv2.inshow("ttu.png", sketch)
