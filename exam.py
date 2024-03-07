import cv2
import dlib

# Function to detect faces
def detect_faces(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use a face detector from dlib
    detector = dlib.get_frontal_face_detector()
    faces = detector(gray)

    return faces

# Function to capture the initial face
def capture_initial_face():
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Detect faces in the frame
        faces = detect_faces(frame)

        # Display the frame with rectangles around detected faces
        for face in faces:
            (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the frame
        cv2.imshow('Capture Initial Face', frame)

        # Break the loop if 'q' key is pressed and a single face is detected
        if cv2.waitKey(1) & 0xFF == ord('q') and len(faces) == 1:
            # Capture the face for reference
            initial_face = faces[0]
            break

    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

    return initial_face

# Main function
def main():
    # Capture the initial face for reference
    initial_face = capture_initial_face()
    print(initial_face)
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Detect faces in the frame
        faces = detect_faces(frame)

        # Display the frame with rectangles around detected faces
        for face in faces:
            (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Check if the current face matches the initial face
        if len(faces) == 1 and faces[0] == initial_face:
            print("Valid face detected!")
        else:
            print("Error: Face changed!")

        # Display the frame
        cv2.imshow('Face Detection', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
