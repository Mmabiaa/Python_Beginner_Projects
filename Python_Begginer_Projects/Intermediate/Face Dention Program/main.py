import cv2
import os

# Check if the XML file exists in the specified path
if not os.path.isfile(r'C:\Users\dell\OneDrive\Documents\Programming\Python\Python_Begginer_Projects\Intermediate\Face Dention Program\haarcascade_frontalface_default.xml'):
    print("XML file not found!")
else:
    print("XML file found!")

# Load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(r'C:\Users\dell\OneDrive\Documents\Programming\Python\Python_Begginer_Projects\Intermediate\Face Dention Program\haarcascade_frontalface_default.xml')

# Check if the cascade is loaded properly
if face_cascade.empty():
    raise IOError("Unable to load the cascade classifier xml file")

# Initialize video capture from webcam (camera 0)
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture frame")
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close any OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
# Author - Mmabiaa
