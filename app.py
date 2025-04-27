import streamlit as st
from openai import OpenAI
import base64
from io import BytesIO
import zipfile
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def generate_images(prompt, n, quality):
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024",
        quality=quality,
        n=n
    )
    return [base64.b64decode(img.b64_json) for img in result.data]

def edit_images(uploaded_img, prompt, n, quality):
    uploaded_img.seek(0)  # 파일 포인터를 처음으로 이동
    result = client.images.edit(
        model="gpt-image-1",
        image=uploaded_img,
        size="1024x1024",
        quality=quality,
        prompt=prompt,
        n=n
    )
    return [base64.b64decode(img.b64_json) for img in result.data]

def main():

    st.set_page_config(page_title="지브리 스타일 이미지 생성기", layout="wide")
    st.title("🌿 지브리 스타일 이미지 생성기")

    # 2 컬럼으로 입력받기
    col1, col2, col3 = st.columns(3)
    with col1:
        theme_input = st.text_input("테마 입력 (쉼표로 구분)", "벚꽃, 겨울, 단풍")
    with col2:
        quality = st.selectbox("이미지 품질", ["high", "medium", "low"], index=0)
    with col3:
        n_variations = st.slider("테마당 생성할 이미지 수", 1, 5, 2)

    # 파일 업로더 추가
    uploaded_file = st.file_uploader("수정할 이미지 업로드 (선택)", type=["png", "jpg", "jpeg", "webp"])

    # 기본 프롬프트 템플릿
    default_prompt_template = (
        " '{theme}' 테마로 지브리 스타일의 환상적인 남산타워 풍경화를 2x2 그리드로 만들어주세요.\n"
        "- 따뜻하고 부드러운 수채화 느낌을 기본으로 하되, 남산타워와 주변 자연 풍경은 선명하고 뚜렷하게 표현해주세요.\n"
        "- 2x2 그리드의 각 장면은 서로 다른 시점과 분위기를 가져야 합니다.\n"
        "- 예를 들어, 하나는 남산타워를 멀리서 본 풍경, 하나는 가까이에서 올려다본 모습, 하나는 주변 숲길과 조화를 이룬 모습, 하나는 일몰 배경 속 실루엣처럼 몽환적인 장면으로 그려주세요.\n"
        "- 자연과 조화를 이루는 신비로운 분위기를 담아주세요.\n"
    )

    ## 지브리 스타일 캐릭터 만들고 싶은 경우, 테마는 딸기,망고,포도

    # default_prompt_template = (
    #     "'{theme}' 테마에서 영감을 받은 지브리 스타일의 판타지 캐릭터 디자인을 2x2 그리드로 만들어주세요.\n"
    #     "- 따뜻하고 부드러운 수채화 느낌을 기본으로 하되, 캐릭터는 선명하고 뚜렷하게 표현해주세요.\n"
    #     "- 색감은 부드럽지만 주요 부분(머리카락, 옷, 소품 등)은 생동감 있고 진하게 채색해주세요\n"
    #     "- 자연 친화적이고 환상적인 의상\n"
    #     "- 다정하고 순수한 표정\n"
    #     "전체적으로 평화롭고 자연과 연결된 세계관 느낌을 유지해주세요."
    # )

    custom_prompt = st.text_area(
        "이미지 생성 프롬프트 (테마는 {theme}로 자동 삽입됩니다)",
        default_prompt_template,
        height=150
    )
    # 이미지 생성 버튼
    if st.button("✨ 이미지 생성하기"):

        themes = [theme.strip() for theme in theme_input.split(",") if theme.strip()]
        all_images = []  # 생성된 모든 이미지를 모을 리스트
        cols = st.columns(3)

        for idx, theme in enumerate(themes):
            with cols[idx % 3]:
                prompt = custom_prompt.format(theme=theme)
                if uploaded_file:
                    st.header(f"{theme} (수정)")
                    images = edit_images(uploaded_file, prompt, n_variations, quality)
                else:
                    st.header(theme)
                    images = generate_images(prompt, n_variations, quality)

                for i, img in enumerate(images):
                    st.image(img, caption=f"{theme} #{i+1}")
                    filename = f"{'edited_' if uploaded_file else ''}{theme}_{i+1}.png"
                    all_images.append((filename, img))

        # 이미지가 있다면 ZIP 파일로 다운로드할 수 있게
        if all_images:
            # 메모리에 ZIP 파일 만들기
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zipf:
                for filename, img_data in all_images:
                    zipf.writestr(filename, img_data)
            zip_buffer.seek(0)

            st.download_button(
                "📦 모든 이미지를 ZIP으로 다운로드",
                data=zip_buffer,
                file_name="ghibli_images.zip",
                mime="application/zip"
            )

if __name__ == "__main__":
    main()
