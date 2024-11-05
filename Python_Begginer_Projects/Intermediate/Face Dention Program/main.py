import cv2

# Load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(r'Intermediate\Face Dention Program\haarcascade_frontalface_default.xml')

# Read the input image (use raw string for path)
image_path = r'image.jpg'

# Check if the image exists and is loaded properly
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not open or find the image.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Face Detection', image)

# Wait for a key press to close the window
cv2.waitKey(0)

# Save the result
cv2.imwrite('Face_detected.jpg', image)

# Close any open OpenCV windows
cv2.destroyAllWindows()
