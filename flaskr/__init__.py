import os
from flask import Flask, request, make_response, jsonify
import time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import cv2
import tensorflow as tf
import numpy as np
import pandas as pd

import mediapipe as mp
from keras.models import load_model


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def root():
        return 'ROOT PAGE'

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/verify')
    def verify():
        global analysed_frame, letters

        ret, frame = cap.read()
        w, h, c = frame.shape

        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with Mediapipe Hands
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            analysisframe = frame
            showframe = analysisframe

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
            analysisframe = cv2.resize(analysisframe, (28, 28))

            nlist = []
            rows, cols = analysisframe.shape
            for i in range(rows):
                for j in range(cols):
                    k = analysisframe[i, j]
                    nlist.append(k)

            datan = pd.DataFrame(nlist).T
            colname = [val for val in range(784)]
            datan.columns = colname

            pixeldata = datan.values
            pixeldata = pixeldata / 255
            pixeldata = pixeldata.reshape(-1, 28, 28, 1)
            prediction = model.predict(pixeldata)
            predarray = np.array(prediction[0])

            letter_prediction_dict = {letters[i]: predarray[i] for i in range(len(letters))}
            predarrayordered = sorted(predarray, reverse=True)
            high1 = predarrayordered[0]

            for key, value in letter_prediction_dict.items():
                if value == high1:
                    predicted_character = key
                    confidence = 100 * value
                    break

            return jsonify({
                'predicted_character': predicted_character,
                'confidence': confidence
            })

        return jsonify({
            'error': 'No hand detected in the frame'
        })

    return app
