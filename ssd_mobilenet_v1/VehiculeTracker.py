class VehicleTracker:
    def __init__(self):
        self.vehicles = {}  # Active vehicles being tracked
        self.lost_vehicles = {}  # Vehicles that have been lost due to occlusion
        self.next_vehicle_id = 0
        self.max_lost_frames = 10  # Maximum number of frames to keep a lost vehicle

    def update(self, detections):
        # Update positions of tracked vehicles and add new vehicles
        # ...

        # Handle lost vehicles
        for vehicle_id, vehicle_data in list(self.lost_vehicles.items()):
            vehicle_data['lost_frames'] += 1
            if vehicle_data['lost_frames'] > self.max_lost_frames:
                del self.lost_vehicles[vehicle_id]
            else:
                # Try to find this vehicle in the current detections
                for detection in detections:
                    if self.is_same_vehicle(vehicle_data, detection):
                        self.vehicles[vehicle_id] = detection
                        del self.lost_vehicles[vehicle_id]
                        break

    def is_same_vehicle(self, vehicle_data, detection):
        # Extract the centroid of the lost vehicle and the new detection
        lost_centroid = vehicle_data['centroid']
        new_centroid = get_centroid(detection)

        # Calculate the Euclidean distance between the two centroids
        distance = np.linalg.norm(np.array(lost_centroid) - np.array(new_centroid))

        # Check if the distance is within an acceptable range
        if distance > MAX_DISTANCE_THRESHOLD:
            return False

        # Compare the size (area of the bounding box)
        lost_size = vehicle_data['size']
        new_size = get_size(detection)

        # Check if the size difference is within an acceptable range
        size_difference = abs(lost_size - new_size)
        if size_difference > MAX_SIZE_DIFFERENCE_THRESHOLD:
            return False

        return True


