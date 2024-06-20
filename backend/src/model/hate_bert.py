# Flask에 필요한 모듈
import sys
from flask import Flask, request, jsonify

# 모델 작동에 필요한 모듈
import torch
from transformers import BertTokenizer, BertForSequenceClassification, BertConfig
import numpy as np

app = Flask(__name__)
@app.route('/bertHate', methods=['POST'])
def bertHate():
    data = request.json
    text = data['body']
    print(text)

    # 모델 경로
    model_path = 'bert-base-multilingual-cased'
    num_labels = 9

    # 모델 저장 경로
    model_save_path = './saving_model/bert_multilabel_model.pth'   

    # 모델과 토크나이저 불러오기
    model, tokenizer = load_model(model_path, num_labels)

    # 디바이스 설정 (GPU가 있으면 GPU, 없으면 CPU 사용)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    # 저장된 모델을 불러오기
    model, tokenizer = load_model(model_path, num_labels)
    # model.load_state_dict(torch.load(model_save_path))
    model.load_state_dict(torch.load(model_save_path, map_location=device))
    model.to(device)

    # 사용자 입력 예측 실행
    predicted_probabilities, binary_predictions = predict_input_text(model, tokenizer, text, device)
    print("Predicted probabilities:", predicted_probabilities)
    print("Binary predictions:", binary_predictions)

    return jsonify(binary_predictions.tolist()) 


# 모델과 토크나이저 로드 함수
def load_model(model_path, num_labels):
    # Pre-trained model과 Tokenizer를 로드합니다.
    model = BertForSequenceClassification.from_pretrained(model_path, num_labels=num_labels)
    tokenizer = BertTokenizer.from_pretrained(model_path)
    return model, tokenizer



# 모델 저장
def save_model(model, path):
    torch.save(model.state_dict(), path)
    print(f"Model saved to {path}")

# 사용자 입력을 받아 문장 예측 함수
def predict_input_text(model, tokenizer, text, device, threshold=0.5):
    model.to(device)
    model.eval()
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    predictions = torch.sigmoid(logits).cpu().numpy()[0]  # sigmoid를 사용하여 확률로 변환
    
    # 예측 결과 해석
    binary_predictions = (predictions > threshold).astype(int)
    class_labels = ['Label_0', 'Label_1', 'Label_2', 'Label_3', 'Label_4', 'Label_5', 'Label_6', 'Label_7', 'Label_8']
    result = {class_labels[i]: predictions[i] for i in range(9)}

    return result, binary_predictions


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9001)
