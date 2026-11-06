import streamlit as st
from google import genai

st.set_page_config(page_title="AI Webtoon & Shorts Script Generator", layout="wide")
st.title("🎬 숏폼 애니메이션 & 웹툰 스크립트 생성기")

# Check if Gemini API key is configured in secrets
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Gemini API key is missing. Please add it to your Streamlit Cloud Secrets.")
else:
    # Initialize Gemini client
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    genre = st.selectbox("장르 선택", ["일상 공감 코미디", "로맨스 / 학원물", "신입사원 / 회사 생활", "판타지 / 환생물"])
    topic = st.text_input("오늘의 에피소드 주제 (예: 지하철에서 아는 사람 만났을 때)")

    if st.button("대본 및 이미지 프롬프트 생성"):
        if not topic:
            st.warning("주제를 입력해주세요.")
        else:
            with st.spinner("Gemini AI가 대본과 장면 프롬프트를 생성 중입니다..."):
                prompt = f"""
                작성 장르: {genre}
                주제: {topic}
                
                다음 형식으로 YouTube Shorts / TikTok용 1분 숏폼 대본을 작성해줘:
                1. 대사 (한국어 2인 대화 / 대사 + 효과음 표현)
                2. 각 장면별 AI 이미지 생성용 영어 프롬프트 (Midjourney/FLUX 스타일, Korean webtoon character style)
                """
                
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                
                st.success("생성 완료!")
                st.markdown(response.text)
