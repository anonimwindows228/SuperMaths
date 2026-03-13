import streamlit as st
from questions import generate_question_batch, get_hint
from database import get_progress, update_progress, award_badges
from badges import check_badges, BADGES
from datetime import date
from styles import GLOBAL_CSS, render_sidebar, render_topnav

SESSION_LENGTH = 10


def _acc_colour(pct: int) -> str:
    if pct >= 80: return "#0f7b45"
    if pct >= 50: return "#c87a00"
    return "#c0392b"


def _generate_question_bank(topic, grade, n):
    """
    Generate all n questions in a single batch API call — fast path.
    Shows a spinner while the single request is in flight.
    """
    with st.spinner(f"Preparing {n} questions on {topic}…"):
        bank = generate_question_batch(topic, grade, n)
    return bank


def show_practice():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    username = st.session_state.username
    topic    = st.session_state.practice_topic
    grade    = st.session_state.practice_grade
    p        = get_progress(username)

    render_sidebar(p)
    render_topnav(st.session_state.get("username", ""))

    if st.button("← Back to Dashboard"):
        st.session_state.practice_topic = None
        for k in ["pr_question_bank", "pr_q_index", "pr_answered", "pr_selected",
                  "pr_show_hint", "pr_hint_text", "pr_hint_question",
                  "pr_session_correct", "pr_session_total", "pr_session_num"]:
            st.session_state.pop(k, None)
        st.rerun()

    st.markdown(f"## 🎮 Practice — {topic}")
    st.caption(f"Each session is {SESSION_LENGTH} questions. Sessions count toward your daily total.")

    if "pr_session_num" not in st.session_state:
        st.session_state.pr_session_num     = 1
        st.session_state.pr_answered        = False
        st.session_state.pr_selected        = None
        st.session_state.pr_show_hint       = False
        st.session_state.pr_session_correct = 0
        st.session_state.pr_session_total   = 0
        st.session_state.pr_q_index         = 0
        st.session_state.pr_question_bank   = None
        if "pr_history" not in st.session_state:
            st.session_state.pr_history = []

    q_in_session = st.session_state.pr_session_total
    session_num  = st.session_state.pr_session_num

    if q_in_session >= SESSION_LENGTH:
        correct = st.session_state.pr_session_correct
        acc     = int(correct / SESSION_LENGTH * 100)
        col     = _acc_colour(acc)

        st.markdown(f"""
        <div style="background:#fff;border:1px solid #dde2ea;border-top:4px solid {col};
                    border-radius:4px;padding:28px 24px;text-align:center;margin-bottom:20px;">
          <div style="font-family:Nunito,sans-serif;font-size:0.8em;font-weight:800;
                      text-transform:uppercase;letter-spacing:1.5px;color:#6b7480;margin-bottom:8px;">
            Session {session_num} Complete
          </div>
          <div style="font-family:Nunito,sans-serif;font-size:3em;font-weight:900;color:{col};line-height:1;">
            {correct}/{SESSION_LENGTH}
          </div>
          <div style="font-size:1.1em;color:#6b7480;margin-top:6px;font-family:Nunito,sans-serif;">
            {acc}% accuracy
          </div>
        </div>""", unsafe_allow_html=True)

        if (not st.session_state.pr_history or
                st.session_state.pr_history[-1]["session"] != session_num):
            st.session_state.pr_history.append({
                "session": session_num, "correct": correct,
                "total": SESSION_LENGTH, "acc": acc,
            })

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("← Back to Dashboard", use_container_width=True):
                st.session_state.practice_topic = None
                for k in ["pr_question_bank", "pr_q_index", "pr_answered", "pr_selected",
                          "pr_show_hint", "pr_hint_text", "pr_hint_question",
                          "pr_session_correct", "pr_session_total", "pr_session_num"]:
                    st.session_state.pop(k, None)
                st.rerun()
        with col_b:
            if st.button(f"Start Session {session_num + 1} →",
                         use_container_width=True, type="primary"):
                st.session_state.pr_session_num     += 1
                st.session_state.pr_question_bank   = None
                st.session_state.pr_q_index         = 0
                st.session_state.pr_answered        = False
                st.session_state.pr_selected        = None
                st.session_state.pr_show_hint       = False
                st.session_state.pr_session_correct = 0
                st.session_state.pr_session_total   = 0
                st.rerun()

        _render_history()
        return

    if st.session_state.pr_question_bank is None:
        st.session_state.pr_question_bank = _generate_question_bank(
            topic, grade, SESSION_LENGTH
        )
        st.session_state.pr_q_index = 0
        st.rerun()

    bank    = st.session_state.pr_question_bank
    q_index = st.session_state.pr_q_index
    question, options, correct = bank[q_index]

    st.markdown(f"""
    <div style="display:flex;align-items:center;justify-content:space-between;
                margin-bottom:6px;font-family:Nunito,sans-serif;">
      <span style="font-size:0.88em;color:#6b7480;font-weight:700;">
        Session {session_num} — Question {q_in_session + 1} of {SESSION_LENGTH}
      </span>
      <span style="font-size:0.88em;color:#1a73e8;font-weight:800;">
        {st.session_state.pr_session_correct} correct so far
      </span>
    </div>""", unsafe_allow_html=True)
    st.progress(q_in_session / SESSION_LENGTH)

    st.subheader(question)

    if not st.session_state.pr_answered:
        col_q, col_hint = st.columns([6, 1])
        with col_hint:
            if st.button("❓ Hint", key="pr_hint_btn", use_container_width=True):
                st.session_state.pr_show_hint = True
        if st.session_state.get("pr_show_hint"):
            with st.spinner("Getting hint…"):
                if ("pr_hint_text" not in st.session_state or
                        st.session_state.get("pr_hint_question") != question):
                    st.session_state.pr_hint_text     = get_hint(question, options)
                    st.session_state.pr_hint_question = question
            st.info(f"💡 **How to approach this:**\n\n{st.session_state.pr_hint_text}")

    answered = st.session_state.pr_answered

    if not answered:
        selected = st.radio(
            "Choose your answer:",
            list(options.keys()),
            format_func=lambda x: f"{x}) {options[x]}",
            key=f"pr_live_{session_num}_{q_in_session}",
        )
        if st.button("Submit Answer", use_container_width=True, type="primary"):
            st.session_state.pr_selected      = selected
            st.session_state.pr_answered      = True
            st.session_state.pr_session_total += 1
            is_correct = (selected == correct)
            if is_correct:
                st.session_state.pr_session_correct += 1

            update_progress(username, 1 if is_correct else 0, 1)

            p2    = get_progress(username)
            today = str(date.today())
            daily = p2.get("daily_answered", 0) if p2.get("daily_date") == today else 0
            new_badges = check_badges(p2, daily_answered=daily)
            award_badges(username, new_badges)
            for b in new_badges:
                bd = BADGES[b]
                st.toast(f"{bd['icon']} Badge unlocked: **{bd['name']}**!", icon="🏅")
            st.rerun()

    else:
        locked     = st.session_state.pr_selected
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
            st.session_state.pr_q_index      += 1
            st.session_state.pr_answered      = False
            st.session_state.pr_selected      = None
            st.session_state.pr_show_hint     = False
            st.session_state.pop("pr_hint_text", None)
            st.rerun()

    _render_history()


def _render_history():
    history = st.session_state.get("pr_history", [])
    if not history:
        return

    st.markdown('<div class="section-title">📊 Session History</div>', unsafe_allow_html=True)

    rows_html = ""
    for s in reversed(history):
        acc   = s["acc"]
        col   = _acc_colour(acc)
        label = f"{s['correct']}/{s['total']}"
        rows_html += f"""
        <div class="session-row">
          <span class="session-num">#{s['session']}</span>
          <span class="session-score">{label}</span>
          <div class="session-acc-bar">
            <div class="session-acc-fill" style="width:{acc}%;background:{col};"></div>
          </div>
          <span class="session-acc-label" style="color:{col};">{acc}%</span>
        </div>"""

    st.markdown(f'<div class="session-history">{rows_html}</div>', unsafe_allow_html=True)
