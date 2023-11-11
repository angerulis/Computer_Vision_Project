import cv2

# Load the TensorFlow model
model = tf.saved_model.load('ssd_mobilenet_v1')

# Function to run inference on a frame
def run_inference(model, image):
    image = np.asarray(image) #
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis,...] # adds a new dimension to the tensor

    model_fn = model.signatures['serving_default'] # retrieves the default serving function
    output_dict = model_fn(input_tensor) #

    return output_dict

def visualize_results(frame, output_dict):
    # Get boxes, scores, and classes from the output
    boxes = output_dict['detection_boxes'][0].numpy()
    classes = output_dict['detection_classes'][0].numpy().astype(np.int64)
    scores = output_dict['detection_scores'][0].numpy()

    # Iterate over all detected objects
    for i in range(len(scores)):
        if scores[i] > 0.5:  # Threshold for detection
            # Scale box to frame dimensions
            h, w, _ = frame.shape
            box = boxes[i] * [h, w, h, w]
            y_min, x_min, y_max, x_max = box.astype('int')

            # Draw rectangle to frame
            frame = cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            # Draw label (assuming class 3 is 'car', modify as per your model's classes)
            if classes[i] == 3:
                label = 'Car'
                frame = cv2.putText(frame, label, (x_min, y_min-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return frame


# Start video capture REAL TIME
# cap = cv2.VideoCapture(0)

# input video
source_video = 'input_video.mp4'
cap = cv2.VideoCapture(source_video)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # If frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break


    # Run object detection
    output_dict = run_inference(model, frame)

    vis_frame = visualize_results(frame, output_dict)

    # Display the resulting frame
    cv2.imshow('Frame Object detected', vis_frame)

    # Press 'q' to exit the video stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release() # frees up the resources associated with the video capture
cv2.destroyAllWindows() #  closes all open HighGUI windows
