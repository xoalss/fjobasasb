import streamlit as st

st.title("🎈 범박이의 첫 번째 앱! ")


st.success("일리아")
st.info("토푸리아")
st.image("https://i.namu.wiki/i/cWV-60JSKEwSOQZLtIFTX68hWuRMdZLsFNYkV2iTHiZ25cJl0rEeE4GBSEvUgy_mmdN6GHFBSogvfGCNtW7fkA.webp")

# st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")

# 페이지 구조용 제목 출력
st.title("메인 제목입니다")
st.header("중간 제목입니다")
st.subheader("하위 제목입니다")

# 수평선 (구분선) 출력
st.markdown("---")  # 또는
st.divider()        # Streamlit >= 1.22 이상에서 가능

# LaTeX 수식 출력
st.latex(r"E = mc^2")
st.latex(r"\int_{a}^{b} x^2 dx = \frac{b^3 - a^3}{3}")

# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")

# 영상 출력
st.video("https://youtu.be/4J7EqOB9sTo?si=S3DgLIUhVp-qFOMn")
st.video("https://youtu.be/soSLgKeBQm4?si=VrjDSJ2JsgBxEuPL")

# 지도 출력
import pandas as pd
df = pd.DataFrame({"lat": [37.5], "lon": [127.0]})
st.map(df, zoom=15)

st.link_button("네이버 바로가기","https://naver.com")

# st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용

    # st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("ℹ️ 자세한 설명 보기"):
    st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")

    # st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("선택한 옵션:", option)

# 정수 혹은 실수 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120, step=1)
st.write("출생년도:", 2026-age)

# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)

# 드롭다운에서 하나 선택
color = st.selectbox("좋아하는 정치색을 선택하세요", ["빨강", "파랑", "주황", "노랑"])
st.write("선택한 색상:", color)

# 여러 개 선택
subjects = st.multiselect("관심 있는 과목을 선택하세요", ["수학", "국어", "체육"])
st.write("선택한 과목:", subjects)

# 날짜 입력
date = st.date_input("날짜를 선택하세요")
st.write("선택한 날짜:", date)

# 시간 입력
time = st.time_input("시간을 선택하세요")
st.write("선택한 시간:", time)

# 카메라로 사진 촬영
image_data = st.camera_input("사진을 찍어보세요")
if image_data:
    st.image(image_data)