# TFP-BE (백엔드)

이 프로젝트는 폭력적인 언어에 무방비하게 노출되는 아동·청소년들을 위한 SNS 필터링 프로그램이다.

총 3개의 기능을 제공한다.

1) Facebook api를 활용해 페이지 피드 불러오기 => 혐오 분류 모델을 사용해 분류 후 클라이언트에 제공
2) 자체 웹소켓 채팅 => 성적/학교폭력 분류 모델을 사용해 분류 후 클라이언트에 제공
3) 포토 앨범 => 폭력적 이미지 분류 모델을 사용해 분류 후 클라이언트에 제공

## 설치 방법

1. 레포지토리를 클론합니다.
    ```bash
    git clone https://github.com/TwitFilterProject/TFP-BE.git
    cd TFP-BE/backend
    ```

2. 필요한 패키지를 설치합니다.
    ```bash
    npm install
    ```

3. 가상환경을 설정합니다.
    ```bash
    conda create --name tfp tensorflow
    conda activate tfp

    pip install falsk
    pip install torch
    pip install transformers
    ```

4. 개발 서버를 실행합니다.

    첫 번째 터미널
    ```bash
    npx nest start
    ```
    두 번째 터미널
    ```bash
    cd src/model
    python hate_bert.py
    ```
    세 번째 터미널
    ```bash
    cd src/model
    python sexual_bert.py
    ```
    네 번째 터미널
    ```bash
    cd src/model
    python img_classification.py
    ```

## 라이선스

MIT License

Copyright (c) 2024 구담인

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
