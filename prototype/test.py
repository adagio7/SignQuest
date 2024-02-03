import cv2
import mediapipe as mp

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False, 
    max_num_hands=1, 
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils

# analysed_frame = ''
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# OpenCV Setup
cap = cv2.VideoCapture(0)  # Use 0 for the default camera
width, height = 640, 480  # Adjust the resolution as needed
cap.set(3, width)
cap.set(4, height)

while cap.isOpened():
    ret, frame = cap.read()
    w, h, c = frame.shape

    if not ret:
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h

            for lm in hand_landmarks.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
            y_min -= 20
            y_max += 20
            x_min -= 20
            x_max += 20
            # cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        # Extract hand landmarks
        # landmarks = results.multi_hand_landmarks[0].landmark

        # TODO: Implement gesture recognition based on the landmarks
        # You can use these landmarks to recognize specific ASL gestures
    # Display the frame
    cv2.imshow("ASL Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the capture and destroy OpenCV windows
cap.release()
cv2.destroyAllWindows()
