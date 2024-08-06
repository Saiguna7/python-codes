import pywhatkit as kit
import cv2

# Generate Handwriting Image
kit.text_to_handwriting("Life Goes On", save_to="handwriting.png")

# Read the generated image
img = cv2.imread("handwriting.png")

# Display the image
cv2.imshow("Text to handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
