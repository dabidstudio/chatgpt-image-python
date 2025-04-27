
# 파이썬으로 ChatGPT 이미지 생성 자동화하기
![image](https://github.com/user-attachments/assets/3c6d492f-1a3d-4433-9ed1-4cc3a759ac2a)

Chat GPT의 최신 이미지 생성 기능이 API로 공개되었습니다! [링크](https://openai.com/index/image-generation-api)

ChatGPT의 강력한 이미지 생성 API를 활용하여,  
**다양한 테마와 스타일의 이미지를 한번에 생성하고 비교**할 수 있는 자동화 프로그램을 파이썬으로 구현합니다.


## 예제 개요

### 1 기본 사용법 예제 (`chatgpt-image-basics.ipynb`)
- 한 장씩 이미지를 생성하는 기본 API 사용법
- 다양한 프롬프트로 여러 이미지를 반복 생성하는 방법

### 2 Streamlit 웹앱 (`app.py`)
- 테마 입력 → 여러 장의 지브리 스타일 이미지 생성
- 다양한 테마/각도/스타일을 동시에 비교할 수 있는 인터페이스 제공
- 생성된 이미지를 한 번에 다운로드하는 기능 포함


## 초기 셋팅

1. 새 폴더를 만든 후 레포지토리 clone 또는 다운로드하기
    ```bash
    git clone https://github.com/dabidstudio/chatgpt-image-python.git . 
    ```

2. [OpenAI API 키 발급](https://github.com/dabidstudio/dabidstudio_guides/blob/main/get-openai-api-key.md)  
   (ChatGPT 이미지 생성 기능은 API 키가 필요합니다.)

3. [조직 인증](https://platform.openai.com/settings/organization/general) 완료하기
   (여권, 민증 등으로 본인 및 조직 인증 필요)

4. API 사용 가격 확인하기
    - 고품질 정사각형 이미지(1024x1024) 1장 생성 비용: 약 0.2 USD (약 300원)
    - 여러 장 생성 시 요금이 빠르게 증가할 수 있으니 주의!
    - [OpenAI Pricing 공식 안내](https://platform.openai.com/docs/pricing)

5. `.env.example` 파일 복사 후, 본인의 API 키를 입력해 `.env` 파일로 저장하기
    ```bash
    OPENAI_API_KEY=발급받은_키_입력
    ```

6. 파이썬 가상환경 생성 및 활성화
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

7. 필수 패키지 설치
    ```bash
    pip install streamlit openai python-dotenv ipykernel
    ```

---

## 폴더 구조

```
├── chatgpt-image-basics.ipynb       # 기본 사용법 예제 (Jupyter Notebook)
├── app.py          # Streamlit 웹앱 (응용 프로젝트)
├── .env.example                     # 환경변수 예시 파일
```

---


# 지금 바로 시작하기

```bash
# 기본 사용법 확인
jupyter notebook chatgpt-image-basics.ipynb

# 웹앱 실행
streamlit run app.py
```

## 참고 자료
- https://openai.com/index/image-generation-api
- https://platform.openai.com/docs/guides/image-generation
- https://platform.openai.com/docs/api-reference/images





