import streamlit as st
from database import get_progress, get_assignments
from badges import BADGES
from datetime import date
from styles import GLOBAL_CSS, render_sidebar, render_topnav, _daily_progress_bar

TOPIC_VIDEOS = {
    "Addition":               ["https://www.youtube.com/watch?v=AuX7nPBqDts"],
    "Subtraction":            ["https://www.youtube.com/watch?v=S2a_EYBqPeI"],
    "Counting":               ["https://www.youtube.com/watch?v=DR-cfDsHCGA"],
    "Number Patterns":        ["https://www.youtube.com/watch?v=Ua2ATkFHkQ4"],
    "Place Value":            ["https://www.youtube.com/watch?v=DqaHhReVpZI"],
    "Multiplication":         ["https://www.youtube.com/watch?v=RVYwunbpMHA"],
    "Division":               ["https://www.youtube.com/watch?v=KGMf314LUc0"],
    "Times Tables":           ["https://www.youtube.com/watch?v=Nz9BzPCn-hM"],
    "Word Problems":          ["https://www.youtube.com/watch?v=UuYAMFvMCJQ"],
    "Mental Maths":           ["https://www.youtube.com/watch?v=IcaxLmWaYmM"],
    "Fractions":              ["https://www.youtube.com/watch?v=n0FZhQ_GkKw"],
    "Decimals":               ["https://www.youtube.com/watch?v=kwh4SD1ToFc"],
    "Rounding":               ["https://www.youtube.com/watch?v=fd-E18EqSVk"],
    "Negative Numbers":       ["https://www.youtube.com/watch?v=JTQl3JGOrZk"],
    "Basic Geometry":         ["https://www.youtube.com/watch?v=302mGpTFwqY"],
    "Basic Algebra":          ["https://www.youtube.com/watch?v=NybHckSEQBI"],
    "Percentages":            ["https://www.youtube.com/watch?v=JeVSmq1Nrpw"],
    "Ratios":                 ["https://www.youtube.com/watch?v=RQ2nYUBVvqI"],
    "Area & Perimeter":       ["https://www.youtube.com/watch?v=AAB0yMDSaMs"],
    "Data & Graphs":          ["https://www.youtube.com/watch?v=_Zh2rMTsX9M"],
    "Linear Equations":       ["https://www.youtube.com/watch?v=9DxrF6Ttws4"],
    "Geometry":               ["https://www.youtube.com/watch?v=302mGpTFwqY"],
    "Probability":            ["https://www.youtube.com/watch?v=uzkc-qNVoOk"],
    "Averages":               ["https://www.youtube.com/watch?v=B1HEzNTGeZ4"],
    "Sequences":              ["https://www.youtube.com/watch?v=VG9ft4_dK24"],
    "Systems of Equations":   ["https://www.youtube.com/watch?v=nok99JOhcjo"],
    "Functions":              ["https://www.youtube.com/watch?v=52tpYl2tTqk"],
    "Indices":                ["https://www.youtube.com/watch?v=-zUmvpkhvW8"],
    "Circle Theorems":        ["https://www.youtube.com/watch?v=EHoMbcFbcC4"],
    "Transformations":        ["https://www.youtube.com/watch?v=bBbAVKfDiD8"],
    "Quadratics":             ["https://www.youtube.com/watch?v=OkmNXy7er84"],
    "Trigonometry":           ["https://www.youtube.com/watch?v=PUB0TaZ7bhA"],
    "Vectors":                ["https://www.youtube.com/watch?v=ml4NSzCQobk"],
    "Simultaneous Equations": ["https://www.youtube.com/watch?v=nok99JOhcjo"],
    "Inequalities":           ["https://www.youtube.com/watch?v=2o5BKBP3HHM"],
    "Statistics":             ["https://www.youtube.com/watch?v=uhxtUt_-GyM"],
    "Advanced Algebra":       ["https://www.youtube.com/watch?v=l3XzepN03KQ"],
    "Surds":                  ["https://www.youtube.com/watch?v=WI3GkLiGMaw"],
    "Graph Sketching":        ["https://www.youtube.com/watch?v=MXV65i9g1Xg"],
    "Proof":                  ["https://www.youtube.com/watch?v=p-0SOWbzUYI"],
    "Pre-Calculus":           ["https://www.youtube.com/watch?v=MNMKpVY0V4s"],
    "Logarithms":             ["https://www.youtube.com/watch?v=Z5myJ8dg_rM"],
    "Binomial Theorem":       ["https://www.youtube.com/watch?v=YNlOf8iwTiI"],
    "Numerical Methods":      ["https://www.youtube.com/watch?v=ER5EzPKdFkE"],
    "Limits":                 ["https://www.youtube.com/watch?v=riXcZT2ICjA"],
    "Differentiation":        ["https://www.youtube.com/watch?v=54_XRjHhZzI"],
    "Integration":            ["https://www.youtube.com/watch?v=rfG8ce4nNh0"],
    "Differential Equations": ["https://www.youtube.com/watch?v=6o7b9yyhH7k"],
    "Complex Numbers":        ["https://www.youtube.com/watch?v=SP-YJe7Vldo"],
    "Advanced Integration":   ["https://www.youtube.com/watch?v=rfG8ce4nNh0"],
    "Series":                 ["https://www.youtube.com/watch?v=YzZUIYRCE38"],
    "Further Calculus":       ["https://www.youtube.com/watch?v=54_XRjHhZzI"],
    "Mechanics":              ["https://www.youtube.com/watch?v=ZM8ECpBuQYE"],
    "Statistics 2":           ["https://www.youtube.com/watch?v=uhxtUt_-GyM"],
    "Parametric Equations":   ["https://www.youtube.com/watch?v=41U1ioTOHuM"],
    "Multivariable Calculus": ["https://www.youtube.com/watch?v=TrcCbdWwCBc"],
    "Linear Algebra":         ["https://www.youtube.com/watch?v=fNk_zzaMoSs"],
    "Real Analysis":          ["https://www.youtube.com/watch?v=sqEyWLGvvdw"],
    "Abstract Algebra":       ["https://www.youtube.com/watch?v=IP7nW_hKB7I"],
    "Number Theory":          ["https://www.youtube.com/watch?v=19SW3P_PRHQ"],
}


def daily_num_class(n):
    if n < 10:  return "num-red"
    if n < 25:  return "num-yellow"
    return "num-green"


def motivational(n):
    msgs = {0: "Start today! 💪", 5: "Warming up!", 10: "Nice work 🔥",
            20: "You're on a roll!", 35: "Crushing it 🚀", 999: "Legend 🏆"}
    for threshold, msg in sorted(msgs.items(), reverse=True):
        if n >= threshold:
            return msg
    return ""


def show_dashboard(cookie_manager):
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    username = st.session_state.username
    p = get_progress(username)

    render_sidebar(p)
    render_topnav(username, cookie_manager)

    if p is None:
        st.markdown("### 🎯 Let's find your starting level")
        st.markdown("Take a quick 10-question placement test to personalise your learning path.")
        _, col_b, _ = st.columns([1, 1.5, 1])
        with col_b:
            if st.button("🧮 Take Placement Test", use_container_width=True, type="primary"):
                st.session_state.show_baseline = True
                st.rerun()
        return

    today          = str(date.today())
    daily_answered = p.get("daily_answered", 0) if p.get("daily_date") == today else 0
    daily_correct  = p.get("daily_correct",  0) if p.get("daily_date") == today else 0
    daily_acc      = int(daily_correct / daily_answered * 100) if daily_answered > 0 else 0
    overall_acc    = int(p["total_correct"] / p["total_answered"] * 100) if p["total_answered"] > 0 else 0

    # ── Top stat cards ──
    c1, c2, c3, c4 = st.columns(4)
    for col, label, value, cls in [
        (c1, "Grade",            f"Grade {p['grade']}", "stat-dark"),
        (c2, "Level",            f"Level {p['level']}", "stat-purple"),
        (c3, "Overall Accuracy", f"{overall_acc}%",     "stat-blue"),
        (c4, "Total Answered",   str(p["total_answered"]), "stat-green"),
    ]:
        with col:
            st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-label">{label}</div>
                    <div class="stat-value {cls}">{value}</div>
                </div>""", unsafe_allow_html=True)

    # ── Daily Progress Bar ──
    st.markdown(_daily_progress_bar(daily_answered), unsafe_allow_html=True)

    # ── Today's Activity ──
    st.markdown('<div class="section-title">📅 Today\'s Activity</div>', unsafe_allow_html=True)
    t1, t2 = st.columns(2)
    with t1:
        nc = daily_num_class(daily_answered)
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">Questions Today</div>
                <div class="{nc}">{daily_answered}</div>
                <div style="font-size:0.84em;color:#6b7280;margin-top:4px">{motivational(daily_answered)}</div>
            </div>""", unsafe_allow_html=True)
    with t2:
        ac  = "num-red" if daily_acc < 50 else "num-yellow" if daily_acc < 75 else "num-green"
        sub = f"From {daily_answered} question{'s' if daily_answered != 1 else ''}" if daily_answered else "No questions yet today"
        st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">Today's Accuracy</div>
                <div class="{ac}">{daily_acc}%</div>
                <div style="font-size:0.84em;color:#6b7280;margin-top:4px">{sub}</div>
            </div>""", unsafe_allow_html=True)

    # ── Badges — flex-wrap grid, works on all screen sizes ──
    st.markdown('<div class="section-title">🏅 Badges</div>', unsafe_allow_html=True)
    earned_badges = set(p.get("badges", []))
    badge_keys    = list(BADGES.keys())

    # Group by category for a nicer layout
    from collections import defaultdict
    by_cat = defaultdict(list)
    for key in badge_keys:
        cat = BADGES[key].get("category", "Other")
        by_cat[cat].append(key)

    for cat in ["Progress", "Levels", "Skill", "Consistency", "Mastery"]:
        keys_in_cat = by_cat.get(cat, [])
        if not keys_in_cat:
            continue
        st.markdown(f'<div style="font-size:0.72em;font-weight:800;text-transform:uppercase;'
                    f'letter-spacing:1.2px;color:#9ba5b7;margin:10px 0 6px 0;'
                    f'font-family:Nunito,sans-serif;">{cat}</div>', unsafe_allow_html=True)
        badge_html = '<div class="badge-grid">'
        for key in keys_in_cat:
            b          = BADGES[key]
            earned     = key in earned_badges
            locked_cls = "" if earned else "badge-locked"
            earned_cls = "badge-card-earned" if earned else ""
            badge_html += f"""
                <div class="badge-card {earned_cls} {locked_cls}" title="{b['desc']}">
                    <div class="badge-ribbon"></div>
                    <div class="badge-disc">
                        <div class="badge-icon">{b['icon']}</div>
                        <div class="badge-name">{b['name']}</div>
                    </div>
                </div>"""
        badge_html += '</div>'
        st.markdown(badge_html, unsafe_allow_html=True)

    st.markdown(
        f'<div class="section-title">📚 Level {p["level"]} Assignments — 5 topics · 2 quizzes each</div>',
        unsafe_allow_html=True
    )

    user_assignments = get_assignments(username)
    if not user_assignments:
        st.info("No assignments found.")
        return

    for a in user_assignments:
        topic   = a["topic"]
        q1_done = a.get("quiz_1_done", False)
        q2_done = a.get("quiz_2_done", False)
        both    = q1_done and q2_done

        row_cls = "topic-row-complete" if both else ""
        icon    = "✅" if both else ("🔄" if q1_done else "📝")
        q1_cls  = "pill-done" if q1_done else "pill-todo"
        q2_cls  = "pill-done" if q2_done else "pill-todo"
        q1_lbl  = f"Quiz 1 ✓ {a.get('quiz_1_score', 0)}/5" if q1_done else "Quiz 1"
        q2_lbl  = f"Quiz 2 ✓ {a.get('quiz_2_score', 0)}/5" if q2_done else "Quiz 2"

        col_info, col_btn = st.columns([4, 1])
        with col_info:
            st.markdown(f"""
                <div class="topic-row {row_cls}">
                    <strong>{icon} {topic}</strong>
                    <div style="margin-top:8px">
                        <span class="quiz-pill {q1_cls}">{q1_lbl}</span>
                        <span class="quiz-pill {q2_cls}">{q2_lbl}</span>
                    </div>
                </div>""", unsafe_allow_html=True)
        with col_btn:
            st.write("")
            st.write("")
            if not both:
                qn = 2 if q1_done else 1
                if st.button(f"Quiz {qn} →", key=f"start_{topic}",
                             use_container_width=True, type="primary"):
                    st.session_state.active_assignment = {**a, "quiz_num": qn}
                    for k in ["assign_index", "assign_score", "assign_answered",
                              "assign_question", "assign_used_hint"]:
                        st.session_state[k] = (
                            0     if "score" in k or "index" in k
                            else None if k == "assign_question"
                            else False
                        )
                    st.rerun()

    st.markdown("""
        <div class="lt-banner">
            ⚡ <strong>Feeling confident?</strong>
            Score 70% or higher on the Level Test to skip straight to the next level.
        </div>""", unsafe_allow_html=True)
    _, col_lt, _ = st.columns([1, 2, 1])
    with col_lt:
        if st.button("🎯 Take Level Test", use_container_width=True, type="primary"):
            st.session_state.show_level_test = True
            st.rerun()

    if all(a.get("quiz_1_done") and a.get("quiz_2_done") for a in user_assignments):
        st.success("🎉 All assignments complete!")

    st.divider()

    st.markdown('<div class="section-title">🎮 Free Practice</div>', unsafe_allow_html=True)
    st.caption("Pick a topic to practise — counts toward your daily total but not assignments.")

    from questions import get_topics_for_level
    topics = get_topics_for_level(p["level"])

    # Responsive grid — max 5 columns, wraps naturally via CSS
    pcols = st.columns(min(len(topics), 5))
    for i, topic in enumerate(topics):
        with pcols[i % len(pcols)]:
            if st.button(f"📖 {topic}", key=f"practice_{topic}", use_container_width=True):
                st.session_state.practice_topic = topic
                st.session_state.practice_grade = p["grade"]
                st.rerun()

    st.markdown('<div class="section-title">🎬 Video Lessons</div>', unsafe_allow_html=True)
    st.caption("Watch a lesson before you practise — one video per topic at your current level.")

    vcols = st.columns(min(len(topics), 5))
    for i, topic in enumerate(topics):
        with vcols[i % len(vcols)]:
            videos = TOPIC_VIDEOS.get(topic, [])
            st.markdown(f'<div class="video-label">📺 {topic}</div>', unsafe_allow_html=True)
            if videos:
                st.video(videos[0])
            else:
                st.caption("No video yet")
