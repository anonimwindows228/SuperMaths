import streamlit as st
from questions import generate_question, parse_question, get_hint
from database import get_progress, update_progress
from styles import GLOBAL_CSS, render_sidebar, render_topnav

def show_practice():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    username = st.session_state.username
    topic    = st.session_state.practice_topic
    grade    = st.session_state.practice_grade
    p        = get_progress(username)

    render_sidebar(p)
    render_topnav(st.session_state.get("username",""))

    if st.button("← Back to Dashboard"):
        st.session_state.practice_topic = None
        for key in ["pr_question", "pr_answered", "pr_show_hint", "pr_hint_text"]:
            st.session_state.pop(key, None)
        st.rerun()

    st.markdown(f"## 🎮 Practice — {topic}")
    st.caption("Unlimited practice. Questions don't count toward your assignments.")

    if "pr_question" not in st.session_state:
        st.session_state.pr_question        = None
        st.session_state.pr_answered        = False
        st.session_state.pr_show_hint       = False
        st.session_state.pr_session_correct = 0
        st.session_state.pr_session_total   = 0

    if st.session_state.pr_question is None:
        with st.spinner("Generating question..."):
            raw = generate_question(topic, grade)
            st.session_state.pr_question  = parse_question(raw)
            st.session_state.pr_show_hint = False

    question, options, correct = st.session_state.pr_question

    if st.session_state.pr_session_total > 0:
        acc = int(st.session_state.pr_session_correct / st.session_state.pr_session_total * 100)
        st.caption(f"This session: {st.session_state.pr_session_correct}/{st.session_state.pr_session_total} correct ({acc}%)")

    st.subheader(question)

    col_q, col_hint = st.columns([6, 1])
    with col_hint:
        if st.button("❓ Hint", key="pr_hint_btn", use_container_width=True):
            st.session_state.pr_show_hint = True
    if st.session_state.get("pr_show_hint"):
        with st.spinner("Getting hint..."):
            if ("pr_hint_text" not in st.session_state or
                    st.session_state.get("pr_hint_question") != question):
                st.session_state.pr_hint_text     = get_hint(question, options)
                st.session_state.pr_hint_question = question
        st.info(f"💡 **How to approach this:**\n\n{st.session_state.pr_hint_text}")

    selected = st.radio("Choose your answer:", list(options.keys()),
                        format_func=lambda x: f"{x}) {options[x]}",
                        key=f"pr_{st.session_state.pr_session_total}")

    if not st.session_state.pr_answered:
        if st.button("Submit Answer", use_container_width=True, type="primary"):
            st.session_state.pr_answered     = True
            st.session_state.pr_session_total += 1
            if selected == correct:
                st.session_state.pr_session_correct += 1
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong! The answer was {correct}) {options[correct]}")
            update_progress(username, 1 if selected == correct else 0, 1)
            st.rerun()
    else:
        if selected == correct:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! The answer was {correct}) {options.get(correct, '')}")
        if st.button("Next Question →", use_container_width=True, type="primary"):
            st.session_state.pr_question  = None
            st.session_state.pr_answered  = False
            st.session_state.pr_show_hint = False
            st.session_state.pop("pr_hint_text", None)
            st.rerun()
