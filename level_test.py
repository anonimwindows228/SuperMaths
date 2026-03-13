import streamlit as st
from questions import generate_question_batch_mixed, get_hint, get_topics_for_level
from database import (get_progress, update_progress, advance_level,
                      delete_assignments, create_assignments, award_badges,
                      increment_level_tests)
from badges import check_badges, BADGES
from styles import GLOBAL_CSS, render_sidebar, render_topnav


def _generate_question_bank(topics, grade, n):
    """Generate all n questions across topics in fast batch calls."""
    with st.spinner(f"Preparing {n} level test questions…"):
        bank = generate_question_batch_mixed(topics, grade, n)
    return bank


def show_level_test():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    username = st.session_state.username
    p        = get_progress(username)
    render_sidebar(p)
    render_topnav(st.session_state.get("username", ""))

    if st.button("← Back to Dashboard"):
        st.session_state.show_level_test = False
        _clear_lt_state()
        st.rerun()

    st.markdown("## ⚡ Level Test")
    st.caption("Score 70% or higher to skip straight to the next level.")

    topics = get_topics_for_level(p["level"])
    total  = 10

    if "lt_index" not in st.session_state:
        st.session_state.lt_index         = 0
        st.session_state.lt_score         = 0
        st.session_state.lt_answered      = False
        st.session_state.lt_selected      = None
        st.session_state.lt_question_bank = None
        st.session_state.lt_show_hint     = False

    current = st.session_state.lt_index

    if current >= total:
        score   = st.session_state.lt_score
        percent = int(score / total * 100)
        update_progress(username, score, total)

        if percent >= 70:
            st.balloons()
            st.success(f"### 🎉 You scored {score}/{total} ({percent}%) — Level passed!")

            increment_level_tests(username)
            new_badges = check_badges(
                get_progress(username),
                level_test_passed=True,
                level_advanced=True,
            )
            award_badges(username, new_badges)
            for b in new_badges:
                bd = BADGES[b]
                st.toast(f"{bd['icon']} Badge unlocked: **{bd['name']}**!", icon="🏅")

            if st.button("Advance to Next Level →", type="primary"):
                delete_assignments(username, p["level"])
                new_level  = advance_level(username)
                new_topics = get_topics_for_level(new_level)
                create_assignments(username, new_level, new_topics)
                _clear_lt_state()
                st.session_state.show_level_test = False
                st.rerun()
        else:
            st.error(f"### You scored {score}/{total} ({percent}%) — 70% needed to pass.")
            st.write("Keep practising your assignments and try again when you're ready!")
            if st.button("Back to Dashboard"):
                _clear_lt_state()
                st.session_state.show_level_test = False
                st.rerun()
        return

    if st.session_state.lt_question_bank is None:
        st.session_state.lt_question_bank = _generate_question_bank(
            topics, p["grade"], total
        )
        st.rerun()

    bank = st.session_state.lt_question_bank
    question, options, correct = bank[current]

    st.progress(current / total)
    st.caption(f"Question {current + 1} of {total}")

    st.subheader(question)

    answered = st.session_state.lt_answered

    if not answered:
        col_q, col_hint = st.columns([6, 1])
        with col_hint:
            if st.button("❓ Hint", key="lt_hint_btn", use_container_width=True):
                st.session_state.lt_show_hint = True
        if st.session_state.get("lt_show_hint"):
            with st.spinner("Getting explanation…"):
                if ("lt_hint_text" not in st.session_state or
                        st.session_state.get("lt_hint_question") != question):
                    st.session_state.lt_hint_text     = get_hint(question, options)
                    st.session_state.lt_hint_question = question
            st.info(f"💡 **How to approach this:**\n\n{st.session_state.lt_hint_text}")

        selected = st.radio(
            "Choose your answer:",
            list(options.keys()),
            format_func=lambda x: f"{x}) {options[x]}",
            key=f"lt_live_{current}",
        )

        if st.button("Submit Answer", use_container_width=True, type="primary"):
            st.session_state.lt_selected = selected
            st.session_state.lt_answered = True
            if selected == correct:
                st.session_state.lt_score += 1
            st.rerun()

    else:
        locked     = st.session_state.lt_selected
        is_correct = (locked == correct)

        for key, text in options.items():
            if key == correct:
                bg, border, weight = "#d4edda", "#0f7b45", "700"
                suffix = " ✅"
            elif key == locked and not is_correct:
                bg, border, weight = "#f8d7da", "#c0392b", "700"
                suffix = " ❌"
            else:
                bg, border, weight = "#f8f9fa", "#dde2ea", "600"
                suffix = ""

            st.markdown(f"""
            <div style="background:{bg};border:2px solid {border};border-radius:4px;
                        padding:13px 16px;margin-bottom:6px;font-family:Nunito,sans-serif;
                        font-size:0.97em;font-weight:{weight};color:#1d2129;display:flex;
                        align-items:center;gap:8px;">
              <span style="min-width:22px;font-weight:800;color:#555;">{key})</span>
              <span>{text}{suffix}</span>
            </div>""", unsafe_allow_html=True)

        if is_correct:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong! The correct answer was **{correct}) {options[correct]}**")

        if st.button("Next Question →", use_container_width=True, type="primary"):
            st.session_state.lt_index    += 1
            st.session_state.lt_answered  = False
            st.session_state.lt_selected  = None
            st.session_state.lt_show_hint = False
            st.session_state.pop("lt_hint_text", None)
            st.rerun()


def _clear_lt_state():
    for k in ["lt_index", "lt_score", "lt_answered", "lt_selected",
              "lt_question_bank", "lt_show_hint", "lt_hint_text", "lt_hint_question"]:
        st.session_state.pop(k, None)
