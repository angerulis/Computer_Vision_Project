import cv2

# Load the pre-trained vehicle detection model (Haarcascades for cars)
car_cascade = cv2.CascadeClassifier("haarcascade_car.xml")

source_video = "traffic_video.mp4"
# Capture video from the camera or local video path
cap = cv2.VideoCapture(source_video)  # Replace with your video source

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Convert the frame to grayscale for better performance
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the frame
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected cars
    for x, y, w, h in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Vehicle Tracking", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object
cap.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()
