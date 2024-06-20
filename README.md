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