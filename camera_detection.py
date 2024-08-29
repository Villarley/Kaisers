import cv2
import numpy as np
import time
from flask import Flask, Response

# Load the pre-trained MobileNet SSD model
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')

# List of classes from the pre-trained model
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# Initialize camera
cap = cv2.VideoCapture(0)  # Use the first camera device

# Initialize Flask app for video streaming
app = Flask(__name__)

def detect_and_report(frame):
    """Detect objects and report risks."""
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.2:  # Confidence threshold
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]

            if label == "person":
                print("Human detected! Initiate evacuation protocol.")
                # More actions can be added here, such as sending a signal
            elif label in ["bottle", "fire", "smoke"]:  # Assume these represent risks
                print(f"Risk detected: {label}. Report and take necessary actions.")
                # More actions can be added here, such as sending a signal

def generate():
    """Video streaming generator function."""
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Perform object detection and reporting
        detect_and_report(frame)

        # Encode the frame for streaming
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Use yield to stream frames to the Flask web server
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    try:
        # Start Flask app for streaming
        app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)
    except KeyboardInterrupt:
        print("Program interrupted by the user.")
    finally:
        # Release the camera and cleanup
        cap.release()
        print("Camera released. Program terminated.")
