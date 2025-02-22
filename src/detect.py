from ultralytics import YOLO
import cv2

# Load the YOLOv8 model (download 'yolov8n.pt' if not present)
model = YOLO("yolov8n.pt")

def detect_vehicles(image_path):
    img = cv2.imread(image_path)
    results = model(image_path)  # Run YOLO detection

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box
            label = r.names[int(box.cls[0])]  # Class name
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    output_path = "static/detected_vehicles.jpg"
    cv2.imwrite(output_path, img)
    return output_path

# Test
if __name__ == "__main__":
    print("Detection saved at:", detect_vehicles("static/accident_scene.jpg"))