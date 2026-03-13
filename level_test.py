import streamlit as st
from questions import generate_question, parse_question, get_hint, get_topics_for_level
from database import (get_progress, update_progress, advance_level,
                      delete_assignments, create_assignments)
from styles import GLOBAL_CSS, render_sidebar, render_topnav

def show_level_test():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    username = st.session_state.username
    p        = get_progress(username)
    render_sidebar(p)
    render_topnav(st.session_state.get("username",""))

    if st.button("← Back to Dashboard"):
        st.session_state.show_level_test = False
        st.rerun()

    st.markdown("## ⚡ Level Test")
    st.caption("Score 70% or higher to skip straight to the next level.")

    topics = get_topics_for_level(p["level"])
    total  = 10

    if "lt_index" not in st.session_state:
        st.session_state.lt_index     = 0
        st.session_state.lt_score     = 0
        st.session_state.lt_answered  = False
        st.session_state.lt_question  = None
        st.session_state.lt_show_hint = False

    current = st.session_state.lt_index

    if current >= total:
        score   = st.session_state.lt_score
        percent = int(score / total * 100)
        update_progress(username, score, total)

        if percent >= 70:
            st.balloons()
            st.success(f"### 🎉 You scored {score}/{total} ({percent}%) — Level passed!")
            if st.button("Advance to Next Level", type="primary"):
                delete_assignments(username, p["level"])
                new_level  = advance_level(username)
                new_topics = get_topics_for_level(new_level)
                create_assignments(username, new_level, new_topics)
                for key in ["lt_index", "lt_score", "lt_answered", "lt_question", "lt_show_hint"]:
                    st.session_state.pop(key, None)
                st.session_state.show_level_test = False
                st.rerun()
        else:
            st.error(f"### You scored {score}/{total} ({percent}%) — 70% needed to pass.")
            st.write("Keep practising your assignments and try again when you're ready!")
            if st.button("Back to Dashboard"):
                for key in ["lt_index", "lt_score", "lt_answered", "lt_question", "lt_show_hint"]:
                    st.session_state.pop(key, None)
                st.session_state.show_level_test = False
                st.rerun()
        return

    st.progress(current / total)
    st.caption(f"Question {current + 1} of {total}")

    if st.session_state.lt_question is None:
        with st.spinner("Generating question..."):
            topic = topics[current % len(topics)]
            raw   = generate_question(topic, p["grade"])
            st.session_state.lt_question  = parse_question(raw)
            st.session_state.lt_show_hint = False

    question, options, correct = st.session_state.lt_question
    st.subheader(question)

    col_q, col_hint = st.columns([6, 1])
    with col_hint:
        if st.button("❓ Hint", key="lt_hint_btn", use_container_width=True):
            st.session_state.lt_show_hint = True
    if st.session_state.get("lt_show_hint"):
        with st.spinner("Getting explanation..."):
            if ("lt_hint_text" not in st.session_state or
                    st.session_state.get("lt_hint_question") != question):
                st.session_state.lt_hint_text     = get_hint(question, options)
                st.session_state.lt_hint_question = question
        st.info(f"💡 **How to approach this:**\n\n{st.session_state.lt_hint_text}")

    selected = st.radio("Choose your answer:", list(options.keys()),
                        format_func=lambda x: f"{x}) {options[x]}",
                        key=f"lt_{current}")

    if not st.session_state.lt_answered:
        if st.button("Submit Answer", use_container_width=True, type="primary"):
            st.session_state.lt_answered = True
            if selected == correct:
                st.session_state.lt_score += 1
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong! The answer was {correct}) {options[correct]}")
            st.rerun()
    else:
        if selected == correct:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! The answer was {correct}) {options.get(correct, '')}")
        if st.button("Next Question →", use_container_width=True, type="primary"):
            st.session_state.lt_index    += 1
            st.session_state.lt_answered  = False
            st.session_state.lt_question  = None
            st.session_state.lt_show_hint = False
            st.session_state.pop("lt_hint_text", None)
            st.rerun()
