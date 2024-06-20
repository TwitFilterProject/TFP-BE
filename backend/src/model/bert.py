import torch
from transformers import BertForSequenceClassification, BertTokenizer, AutoModelForTokenClassification
# from flask import Flask, request, jsonify

# 모델 로드
num_labels=9
model_path = 'bert-base-multilingual-cased'
model = BertForSequenceClassification.from_pretrained(model_path, num_labels=num_labels)
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# saved_model_path = 'saving_folder/BERT_model.pt'
# model.load_state_dict(torch.load(saved_model_path, map_location=device))
# model.to(device)

model = AutoModelForTokenClassification.from_pretrained('saving_folder', num_labels=num_labels)
model.to(device)

model = BertForSequenceClassification.from_pretrained(model_path)

# Tokenizer를 로드합니다
tokenizer = BertTokenizer.from_pretrained(model_path)

# 추론 함수 정의
def ner_inference(text):
    model.eval()
    inputs = tokenizer(text, return_tensors='pt').to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_labels = torch.argmax(logits, dim=1).tolist()
    return predicted_labels


# 예시 문장으로 추론 수행
text = "안녕"
predicted_labels = ner_inference(text)
print(predicted_labels)