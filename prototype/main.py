import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import cv2
import tensorflow as tf
import numpy as np
import pandas as pd

import mediapipe as mp
from keras.models import load_model

model = load_model('models/smnist.keras')
model.summary()

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils

analysed_frame = ''
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Initialize the camera
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
        analysisframe = frame
        showframe = analysisframe
        cv2.imshow("Frame", showframe)

        framergbanalysis = cv2.cvtColor(analysisframe, cv2.COLOR_BGR2RGB)
        results = hands.process(framergbanalysis)
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                x_max = 0
                y_max = 0
                x_min = w
                y_min = h

                for lmanalysis in landmarks.landmark:
                    x, y = int(lmanalysis.x * w), int(lmanalysis.y * h)
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

                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        analysisframe = cv2.cvtColor(analysisframe, cv2.COLOR_BGR2GRAY)
        analysisframe = analysisframe[max(x_min, 0): x_max, max(y_min, 0):y_max]
        analysisframe = cv2.resize(analysisframe,(28,28))

        nlist = []
        rows,cols = analysisframe.shape
        for i in range(rows):
            for j in range(cols):
                k = analysisframe[i,j]
                nlist.append(k)

        datan = pd.DataFrame(nlist).T
        colname = []
        for val in range(784):
            colname.append(val)
        datan.columns = colname

        pixeldata = datan.values
        pixeldata = pixeldata / 255
        pixeldata = pixeldata.reshape(-1,28,28,1)
        prediction = model.predict(pixeldata)
        predarray = np.array(prediction[0])

        letter_prediction_dict = {letters[i]: predarray[i] for i in range(len(letters))}
        predarrayordered = sorted(predarray, reverse=True)
        high1 = predarrayordered[0]
        high2 = predarrayordered[1]
        high3 = predarrayordered[2]
        for key,value in letter_prediction_dict.items():
            if value==high1:
                print("Predicted Character 1: ", key)
                print('Confidence 1: ', 100*value)
            # elif value==high2:
            #     print("Predicted Character 2: ", key)
            #     print('Confidence 2: ', 100*value)
            # elif value==high3:
            #     print("Predicted Character 3: ", key)
            #     print('Confidence 3: ', 100*value)
        time.sleep(5)

    # Display the frame
    cv2.imshow("ASL Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the capture and destroy OpenCV windows
cap.release()
cv2.destroyAllWindows()
