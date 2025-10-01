# study_planner_app_local.py
import streamlit as st
import pandas as pd
import datetime
import random

st.set_page_config(page_title="AI 없는 학습 플래너", layout="wide")

# ---------------------------
# 상태 초기화
# ---------------------------
def init_state():
    if "schedule" not in st.session_state:
        st.session_state.schedule = pd.DataFrame(columns=["date","start","end","topic","notes","duration_min"])
    if "logs" not in st.session_state:
        st.session_state.logs = []
init_state()

# ---------------------------
# 간단 피드백 생성 함수 (규칙 기반)
# ---------------------------
def simple_feedback(study_text):
    strengths, improvements, actions = [], [], []

    if "이해" in study_text:
        strengths.append("핵심 개념을 잘 이해함 👍")
    if "정리" in study_text:
        strengths.append("내용을 스스로 요약 정리했음")
    if "풀이" in study_text:
        strengths.append("문제 풀이를 시도했음")

    if "헷갈" in study_text or "어려" in study_text:
        improvements.append("헷갈린 개념을 추가 복습하세요.")
    if "못 풀" in study_text:
        improvements.append("못 푼 문제를 다시 복습하고 유사 문제를 풀어보세요.")

    if not strengths:
        strengths.append("기록을 남긴 것 자체가 훌륭합니다 🎉")

    if not improvements:
        improvements.append("큰 어려움은 보이지 않습니다. 꾸준히 유지하세요.")

    actions = [
        "20분 복습 시간 확보",
        "5문제 더 풀어보기",
        "내일은 오늘 헷갈린 개념 복습"
    ]
    return {
        "summary": "간단 자동 피드백입니다.",
        "strengths": strengths,
        "improvements": improvements,
        "actions": random.sample(actions, 2),
        "confidence": "데모"
    }

# ---------------------------
# UI
# ---------------------------
st.title("📝 오프라인 학습 플래너 (OpenAI 없이)")

study_date = st.date_input("학습 날짜", value=datetime.date.today())
study_text = st.text_area("오늘 공부한 내용을 적어보세요", height=250)

if st.button("피드백 받기"):
    feedback = simple_feedback(study_text)
    st.session_state.logs.append({"date": str(study_date), "text": study_text, "feedback": feedback})
    st.success("피드백이 생성되었습니다.")

if st.session_state.logs:
    last = st.session_state.logs[-1]
    fb = last["feedback"]
    st.markdown(f"### 📌 피드백 요약 — {last['date']}")
    st.write(f"**요약:** {fb['summary']}")
    st.write("**잘 이해한 부분**")
    for s in fb["strengths"]:
        st.write("- " + s)
    st.write("**추가 학습 필요**")
    for i in fb["improvements"]:
        st.write("- " + i)
    st.write("**권장 액션**")
    for a in fb["actions"]:
        st.write("- " + a)

# 일정 관리
st.subheader("📅 일정 관리")
with st.form("add_session"):
    s_date = st.date_input("날짜", value=study_date)
    col1, col2 = st.columns(2)
    with col1:
        s_start = st.time_input("시작 시간", value=datetime.time(19,0))
    with col2:
        s_end = st.time_input("종료 시간", value=datetime.time(20,0))
    s_topic = st.text_input("주제")
    s_notes = st.text_input("메모")
    if st.form_submit_button("세션 추가"):
        dur = int((datetime.datetime.combine(s_date,s_end)-datetime.datetime.combine(s_date,s_start)).total_seconds()//60)
        new_row = {"date": str(s_date), "start": s_start.strftime("%H:%M"), "end": s_end.strftime("%H:%M"), "topic": s_topic, "notes": s_notes, "duration_min": dur}
        st.session_state.schedule = pd.concat([st.session_state.schedule, pd.DataFrame([new_row])], ignore_index=True)
        st.success("세션이 추가되었습니다.")

st.dataframe(st.session_state.schedule, use_container_width=True)
