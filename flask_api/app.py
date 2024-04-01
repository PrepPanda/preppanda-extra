# server.py
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import cv2
import numpy as np
import os

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@socketio.on('frame')
def handle_frame(image_data):
    # Convert the base64 encoded image data to bytes
    image_bytes = np.frombuffer(image_data, dtype=np.uint8)
    
    # Decode the image bytes into a numpy array
    frame = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    
    # Convert the image to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
    num_faces = len(faces)
    print(num_faces)

    # Emit the face count back to the client
    emit('face_count', num_faces)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=True, log_output=True)

