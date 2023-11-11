class VehicleTracker:
    def __init__(self):
        self.next_vehicle_id = 0
        self.vehicles = {}

    def update(self, detections):
        # detections would be a list of bounding box coordinates
        # Implement logic to update the position of tracked vehicles
        # and to add new vehicles if they don't match existing ones

        # Example logic to assign IDs to new vehicles
        for detection in detections:
            if self.is_new_vehicle(detection):
                self.vehicles[self.next_vehicle_id] = detection
                self.next_vehicle_id += 1

    def is_new_vehicle(self, detection):
        # Implement logic to check if a detection corresponds to a new vehicle
        # This could be based on distance from existing vehicles, size, etc.
        pass

# In your main loop
vehicle_tracker = VehicleTracker()

while True:
    # existing video capture and object detection code

    detections = extract_detections(output_dict)  # You need to write this function
    vehicle_tracker.update(detections)

    # existing code to display frames
