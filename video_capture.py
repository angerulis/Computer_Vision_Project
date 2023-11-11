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

# Start video capture
cap = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # If frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break


    # Run object detection
    output_dict = run_inference(model, frame)

    # ToDo:- Visualization of the results of a detection.
    #      - write this function to draw bounding boxes and labels based on the output_dict

    vis_frame = visualize_results(frame, output_dict)

    # Display the resulting frame
    cv2.imshow('Frame Object detected', vis_frame)

    # Press 'q' to exit the video stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release() # frees up the resources associated with the video capture
cv2.destroyAllWindows() #  closes all open HighGUI windows
