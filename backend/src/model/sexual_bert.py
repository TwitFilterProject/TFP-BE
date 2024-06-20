# Flask에 필요한 모듈
import sys
from flask import Flask, request, jsonify

# 모델 작동에 필요한 모듈
import torch
from transformers import BertTokenizer, BertForSequenceClassification, BertConfig

app = Flask(__name__)
@app.route('/bertSexual', methods=['POST'])
def bertSexual():
    data = request.json
    text = data['body']

    # 모델 로드
    model_stage1_path = './saving_model/final_stage1_model.pth'
    model_stage2_path = './saving_model/final_stage2_model.pth'

    model_stage1 = load_model(BertForSequenceClassification, model_stage1_path, device)
    model_stage2 = load_model(BertForSequenceClassification, model_stage2_path, device)

    # 예측
    predicted_class, probabilities = predict_class(text, model_stage1, model_stage2, tokenizer, max_length=128, device=device)

    print(f"입력 문장: {text}")
    print(f"예측된 클래스: {predicted_class}")
    print(f"클래스 확률: {probabilities}")

    return jsonify(predicted_class) 


# 토크나이저 및 디바이스 설정
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 모델 로드 함수 정의
def load_model(model_class, model_path, device):
    config = BertConfig.from_pretrained('bert-base-multilingual-cased')
    model = model_class(config)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    return model

# 예측 함수 정의
def predict_class(sentence, model_stage1, model_stage2, tokenizer, max_length, device):
    model_stage1.eval()
    model_stage2.eval()

    encoding = tokenizer.encode_plus(
        sentence,
        add_special_tokens=True,
        max_length=max_length,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )

    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)

    # Stage 1 예측 (SEXUAL 여부)
    with torch.no_grad():
        outputs_stage1 = model_stage1(input_ids, attention_mask=attention_mask)
        probabilities_stage1 = torch.nn.functional.softmax(outputs_stage1.logits, dim=-1)
        predicted_class_stage1 = torch.argmax(probabilities_stage1, dim=1).item()

    if predicted_class_stage1 == 1:
        return "SEXUAL", probabilities_stage1.cpu().numpy()

    # Stage 2 예측 (Non-sexual 데이터)
    with torch.no_grad():
        outputs_stage2 = model_stage2(input_ids, attention_mask=attention_mask)
        probabilities_stage2 = torch.nn.functional.softmax(outputs_stage2.logits, dim=-1)
        predicted_class_stage2 = torch.argmax(probabilities_stage2, dim=1).item()

    if predicted_class_stage2 == 0:
        return "IMMORAL_NONE", probabilities_stage2.cpu().numpy()
    else:
        return "SCHOOL VIOLENCE", probabilities_stage2.cpu().numpy()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)