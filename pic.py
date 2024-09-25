import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = r"C:\Users\enjyg\OneDrive\Desktop\Image_20240925094724.jpg"

image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("The image path is incorrect or the image does not exist.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blur, 50, 150)

kernel = np.ones((3, 3), np.uint8)
bold_edges = cv2.dilate(edges, kernel, iterations=2)

inverted_bold_edges = cv2.bitwise_not(bold_edges)

plt.figure(figsize=(8, 8))
plt.imshow(inverted_bold_edges, cmap='gray')
plt.axis('off')  
plt.show()
