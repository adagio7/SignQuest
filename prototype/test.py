import cv2
import mediapipe as mp

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)

# OpenCV Setup
cap = cv2.VideoCapture(0)  # Use 0 for the default camera
width, height = 640, 480  # Adjust the resolution as needed
cap.set(3, width)
cap.set(4, height)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        # Extract hand landmarks
        landmarks = results.multi_hand_landmarks[0].landmark

        # TODO: Implement gesture recognition based on the landmarks
        # You can use these landmarks to recognize specific ASL gestures

    # Display the frame
    cv2.imshow("ASL Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the capture and destroy OpenCV windows
cap.release()
cv2.destroyAllWindows()
