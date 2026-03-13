import streamlit as st
from questions import generate_question_batch, get_hint, get_topics_for_level
from database import (complete_quiz, all_assignments_complete, advance_level,
                      create_assignments, delete_assignments, get_progress,
                      update_progress, award_badges, get_completed_topics)
from badges import check_badges, BADGES
from datetime import date
from styles import GLOBAL_CSS, render_sidebar, render_topnav


def _generate_question_bank(topic, grade, n):
    """Generate all n questions in a single batch API call."""
    with st.spinner(f"Preparing {n} questions on {topic}…"):
        bank = generate_question_batch(topic, grade, n)
    return bank


def show_assignment(assignment):
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    topic    = assignment["topic"]
    quiz_num = assignment.get("quiz_num", 1)
    username = st.session_state.username
    total    = 5

    p = get_progress(username)
    render_sidebar(p)
    render_topnav(st.session_state.get("username", ""))

    _assign_defaults = {
        "assign_index":          0,
        "assign_score":          0,
        "assign_answered":       False,
        "assign_selected":       None,
        "assign_question_bank":  None,
        "assign_used_hint":      False,
        "assign_progress_saved": False,
    }
    for _k, _v in _assign_defaults.items():
        if _k not in st.session_state:
            st.session_state[_k] = _v

    current = st.session_state.assign_index

    if current >= total:
        score = st.session_state.assign_score
        st.success(f"### ✅ Quiz {quiz_num} complete! You scored **{score}/{total}**")

        if not st.session_state.assign_progress_saved:
            update_progress(username, score, total)
            complete_quiz(username, topic, quiz_num, score)
            st.session_state.assign_progress_saved = True

            p     = get_progress(username)
            today = str(date.today())
            daily = p.get("daily_answered", 0) if p.get("daily_date") == today else 0
            completed_topics = get_completed_topics(username)
            new_badges = check_badges(
                p, quiz_score=score,
                used_hint=st.session_state.assign_used_hint,
                daily_answered=daily,
                completed_topics=completed_topics,
            )
            award_badges(username, new_badges)
            if new_badges:
                for b in new_badges:
                    bd = BADGES[b]
                    st.toast(f"{bd['icon']} Badge unlocked: **{bd['name']}**!", icon="🏅")

        p = get_progress(username)
        if all_assignments_complete(username, p["level"]):
            st.balloons()
            st.success("🎉 All assignments complete! You've unlocked the next level!")
            if st.button("Advance to Next Level →", type="primary"):
                delete_assignments(username, p["level"])
                new_level  = advance_level(username)
                new_topics = get_topics_for_level(new_level)
                create_assignments(username, new_level, new_topics)

                new_badges2 = check_badges(get_progress(username), level_advanced=True)
                award_badges(username, new_badges2)
                for b in new_badges2:
                    bd = BADGES[b]
                    st.toast(f"{bd['icon']} Badge unlocked: **{bd['name']}**!", icon="🏅")

                _clear_assign_state()
                st.rerun()
        else:
            if st.button("← Back to Dashboard", type="primary"):
                _clear_assign_state()
                st.rerun()
        return

    if st.button("← Back"):
        _clear_assign_state()
        st.rerun()

    st.markdown(f"### 📝 {topic} — Quiz {quiz_num}")
    st.progress(current / total)
    st.caption(f"Question {current + 1} of {total}")

    if st.session_state.assign_question_bank is None:
        st.session_state.assign_question_bank = _generate_question_bank(
            topic, p["grade"], total
        )
        st.rerun()

    bank = st.session_state.assign_question_bank
    question, options, correct = bank[current]

    st.subheader(question)

    answered = st.session_state.assign_answered

    if not answered:
        col_q, col_hint = st.columns([6, 1])
        with col_hint:
            if st.button("❓ Hint", use_container_width=True):
                st.session_state.show_hint        = True
                st.session_state.assign_used_hint = True

        if st.session_state.get("show_hint"):
            with st.spinner("Getting explanation…"):
                if ("hint_text" not in st.session_state or
                        st.session_state.get("hint_question") != question):
                    st.session_state.hint_text     = get_hint(question, options)
                    st.session_state.hint_question = question
            st.info(f"💡 **How to approach this:**\n\n{st.session_state.hint_text}")

        selected = st.radio(
            "Choose your answer:",
            list(options.keys()),
            format_func=lambda x: f"{x}) {options[x]}",
            key=f"assign_live_{current}",
        )

        if st.button("Submit Answer", use_container_width=True, type="primary"):
            st.session_state.assign_selected = selected
            st.session_state.assign_answered = True
            if selected == correct:
                st.session_state.assign_score += 1
            st.rerun()

    else:
        locked     = st.session_state.assign_selected
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
            st.session_state.assign_index   += 1
            st.session_state.assign_answered = False
            st.session_state.assign_selected = None
            st.session_state.show_hint       = False
            st.session_state.pop("hint_text", None)
            st.rerun()


def _clear_assign_state():
    for k in ["assign_index", "assign_score", "assign_answered", "assign_selected",
              "assign_question_bank", "assign_used_hint", "active_assignment",
              "assign_progress_saved", "show_hint", "hint_text", "hint_question"]:
        st.session_state.pop(k, None)
