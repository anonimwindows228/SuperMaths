import streamlit as st
from questions import generate_question, parse_question, get_hint, get_topics_for_level
from database import (complete_quiz, all_assignments_complete, advance_level,
                      create_assignments, delete_assignments, get_progress,
                      update_progress, award_badges)
from badges import check_badges, BADGES
from datetime import date
from styles import GLOBAL_CSS, render_sidebar, render_topnav

def show_assignment(assignment):
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    topic    = assignment["topic"]
    quiz_num = assignment.get("quiz_num", 1)
    username = st.session_state.username
    total    = 5

    p = get_progress(username)
    render_sidebar(p)
    render_topnav(st.session_state.get("username",""))

    if "assign_index" not in st.session_state:
        st.session_state.assign_index     = 0
        st.session_state.assign_score     = 0
        st.session_state.assign_answered  = False
        st.session_state.assign_question  = None
        st.session_state.assign_used_hint = False

    current = st.session_state.assign_index

    if current >= total:
        score = st.session_state.assign_score
        st.success(f"### ✅ Quiz {quiz_num} complete! You scored **{score}/{total}**")
        update_progress(username, score, total)
        complete_quiz(username, topic, quiz_num, score)

        p = get_progress(username)
        today = str(date.today())
        daily = p.get("daily_answered", 0) if p.get("daily_date") == today else 0
        new_badges = check_badges(p, quiz_score=score,
                                  used_hint=st.session_state.assign_used_hint,
                                  daily_answered=daily)
        award_badges(username, new_badges)
        if new_badges:
            for b in new_badges:
                bd = BADGES[b]
                st.toast(f"{bd['icon']} Badge unlocked: **{bd['name']}**!", icon="🏅")

        if all_assignments_complete(username, p["level"]):
            st.balloons()
            st.success("🎉 All assignments complete! You've unlocked the next level!")
            if st.button("Advance to Next Level", type="primary"):
                delete_assignments(username, p["level"])
                new_level  = advance_level(username)
                new_topics = get_topics_for_level(new_level)
                create_assignments(username, new_level, new_topics)
                new_badges2 = check_badges(get_progress(username))
                award_badges(username, new_badges2)
                for k in ["assign_index", "assign_score", "assign_answered",
                          "assign_question", "assign_used_hint", "active_assignment"]:
                    st.session_state.pop(k, None)
                st.rerun()
        else:
            if st.button("Back to Dashboard", type="primary"):
                for k in ["assign_index", "assign_score", "assign_answered",
                          "assign_question", "assign_used_hint", "active_assignment"]:
                    st.session_state.pop(k, None)
                st.rerun()
        return

    if st.button("← Back"):
        for k in ["assign_index", "assign_score", "assign_answered",
                  "assign_question", "assign_used_hint", "active_assignment"]:
            st.session_state.pop(k, None)
        st.rerun()

    st.markdown(f"### 📝 {topic} — Quiz {quiz_num}")
    st.progress(current / total)
    st.caption(f"Question {current + 1} of {total}")

    if st.session_state.assign_question is None:
        with st.spinner("Generating question..."):
            p   = get_progress(username)
            raw = generate_question(topic, p["grade"])
            st.session_state.assign_question = parse_question(raw)
            st.session_state.show_hint       = False

    question, options, correct = st.session_state.assign_question
    st.subheader(question)

    col_q, col_hint = st.columns([6, 1])
    with col_hint:
        if st.button("❓ Hint", use_container_width=True):
            st.session_state.show_hint        = True
            st.session_state.assign_used_hint = True

    if st.session_state.get("show_hint"):
        with st.spinner("Getting explanation..."):
            if ("hint_text" not in st.session_state or
                    st.session_state.get("hint_question") != question):
                st.session_state.hint_text     = get_hint(question, options)
                st.session_state.hint_question = question
        st.info(f"💡 **How to approach this:**\n\n{st.session_state.hint_text}")

    selected = st.radio("Choose your answer:", list(options.keys()),
                        format_func=lambda x: f"{x}) {options[x]}",
                        key=f"assign_{current}")

    if not st.session_state.assign_answered:
        if st.button("Submit Answer", use_container_width=True, type="primary"):
            st.session_state.assign_answered = True
            if selected == correct:
                st.session_state.assign_score += 1
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
            st.session_state.assign_index    += 1
            st.session_state.assign_answered  = False
            st.session_state.assign_question  = None
            st.session_state.show_hint        = False
            st.session_state.pop("hint_text", None)
            st.rerun()
