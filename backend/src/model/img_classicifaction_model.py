# Flask에 필요한 모듈
import sys
from flask import Flask, request, jsonify

# 모델 작동에 필요한 모듈
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
@app.route('/imageClassification', methods=['POST'])
def imageClassification():

    # 저장된 모델 불러오기
    class_labels = ['Non-Violence', 'Violence'] 
    loaded_model = tf.keras.models.load_model('./saving_model/violence_model.h5')
    img_paths = ['violence1.png', 'violence2.png', 'violence3.png', 'violence4.png',
                'nonViolence1.png', 'nonViolence2.png',
                'nonViolence3.png', 'nonViolence4.png']  # 예측할 이미지 경로
    
    # 결과를 저장할 배열 초기화
    predictions_arr = []

    for img_path in img_paths:
        prediction = predict_image(loaded_model, img_path)
        predicted_class, predicted_probability, non_violence_prob, violence_prob = interpret_prediction(prediction)
        print(f"Image: {img_path}")
        print(f"Raw prediction: {prediction}")
        print(f"Predicted: {predicted_class} with probability {predicted_probability:.2f}")
        print(f"Non-Violence probability: {non_violence_prob:.2f}")
        print(f"Violence probability: {violence_prob:.2f}")
        print("\n")
        predictions_arr.append(predicted_class)

    return jsonify(predictions_arr) 

# 이미지 전처리 함수
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # 모델 학습 시 사용된 이미지 크기와 동일하게 설정
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # 정규화 (모델 학습 시 사용된 동일한 정규화 방법)
    return img_array

# 이미지 예측 함수
def predict_image(model, img_path):
    preprocessed_img = preprocess_image(img_path)
    prediction = model.predict(preprocessed_img)
    return prediction

# 예측 결과 해석 함수
def interpret_prediction(prediction):
    class_labels = ['Non-Violence', 'Violence']  # 클래스 레이블을 학습 시 사용한 순서에 맞게 정의
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    predicted_class = class_labels[predicted_class_index]
    predicted_probability = prediction[0][predicted_class_index]
    
    # 각 클래스의 확률 출력
    non_violence_prob = prediction[0][0]
    violence_prob = prediction[0][1]

    return predicted_class, predicted_probability, non_violence_prob, violence_prob


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9002)