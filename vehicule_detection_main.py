import tensorflow as tf
import cv2

# Load the model from Tensorflow's model
model = tf.saved_model.load('ssd_mobilenet_v1_coco_2017_11_17/saved_model')

# Video Capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    #break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()