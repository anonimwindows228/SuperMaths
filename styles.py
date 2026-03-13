GLOBAL_CSS = """
<style>
    /* ── Base ── */
    body, .stApp {
        background: #f0f2f5 !important;
        color: #1a1a2e !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
    }

    /* ── Force sidebar always open & hide ALL collapse controls ── */
    section[data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 2px solid #e5e7eb !important;
        min-width: 260px !important;
        max-width: 260px !important;
        transform: none !important;
        visibility: visible !important;
        display: block !important;
    }
    section[data-testid="stSidebar"][aria-expanded="false"] {
        margin-left: 0 !important;
        transform: translateX(0) !important;
        min-width: 260px !important;
    }
    button[data-testid="stSidebarNavCollapseButton"],
    button[data-testid="collapsedControl"],
    button[data-testid="stSidebarCollapseButton"],
    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"],
    .stSidebarCollapseButton,
    button[title="Collapse sidebar"],
    button[title="Expand sidebar"],
    button[aria-label="Collapse sidebar"],
    button[aria-label="Expand sidebar"],
    section[data-testid="stSidebar"] button[kind="header"] {
        display: none !important;
        visibility: hidden !important;
        pointer-events: none !important;
    }

    /* ── Top nav bar ── */
    .ka-nav {
        background: #1b1b32;
        padding: 0 28px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 54px;
        margin-bottom: 24px;
        border-bottom: 3px solid #2563eb;
    }
    .ka-logo-wrap {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .ka-logo-icon {
        width: 32px;
        height: 32px;
        background: #2563eb;
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1em;
    }
    .ka-logo-text {
        font-size: 1.2em;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: -0.3px;
    }
    .ka-logo-text span { color: #60a5fa; }
    .ka-user {
        display: flex;
        align-items: center;
        gap: 14px;
        font-size: 0.88em;
        color: #9ca3af;
    }
    .ka-user-badge {
        background: #2563eb;
        color: #fff;
        font-size: 0.72em;
        font-weight: 700;
        padding: 2px 9px;
        border-radius: 3px;
        letter-spacing: 0.5px;
    }

    /* ── Main content ── */
    .main .block-container {
        padding-top: 0 !important;
        max-width: 1100px !important;
    }

    /* ── Stat cards ── */
    .stat-card {
        background: #ffffff;
        border: 1px solid #d1d5db;
        border-left: 4px solid #2563eb;
        border-radius: 4px;
        padding: 18px 16px;
        text-align: center;
    }
    .stat-label {
        font-size: 0.68em;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 1.1px;
        font-weight: 600;
    }
    .stat-value  { font-size: 1.9em; font-weight: 800; margin: 5px 0 2px 0; }
    .stat-green  { color: #059669; }
    .stat-purple { color: #7c3aed; }
    .stat-blue   { color: #2563eb; }
    .stat-dark   { color: #111827; }

    /* ── Section titles ── */
    .section-title {
        font-size: 0.95em;
        font-weight: 700;
        color: #111827;
        margin: 26px 0 10px 0;
        display: flex;
        align-items: center;
        gap: 7px;
        border-bottom: 2px solid #e5e7eb;
        padding-bottom: 6px;
    }

    /* ── Topic rows ── */
    .topic-row {
        background: #ffffff;
        border: 1px solid #d1d5db;
        border-left: 4px solid #2563eb;
        border-radius: 4px;
        padding: 13px 16px;
        margin-bottom: 7px;
    }
    .topic-row-complete { border-left-color: #059669 !important; }
    .topic-row strong   { color: #111827 !important; }

    /* ── Quiz pills ── */
    .quiz-pill {
        display: inline-block;
        padding: 2px 9px;
        border-radius: 3px;
        font-size: 0.74em;
        margin-right: 5px;
        font-weight: 600;
    }
    .pill-done { background: #d1fae5; color: #065f46; border: 1px solid #6ee7b7; }
    .pill-todo { background: #f3f4f6; color: #6b7280; border: 1px solid #d1d5db; }

    /* ── Badge cards ── */
    .badge-card {
        background: #ffffff;
        border-radius: 4px;
        padding: 12px 8px;
        text-align: center;
        border: 1px solid #d1d5db;
        height: 100%;
    }
    .badge-card-earned { border-color: #059669; background: #f0fdf4; }
    .badge-icon   { font-size: 1.8em; }
    .badge-name   { font-size: 0.75em; font-weight: 700; color: #111827; margin-top: 5px; }
    .badge-desc   { font-size: 0.66em; color: #6b7280; margin-top: 2px; }
    .badge-locked { opacity: 0.28; }

    /* ── Level test banner ── */
    .lt-banner {
        background: #eff6ff;
        border: 1px solid #93c5fd;
        border-left: 4px solid #2563eb;
        border-radius: 4px;
        padding: 14px 18px;
        margin: 14px 0;
        color: #1e3a5f;
        font-size: 0.93em;
    }

    /* ── Video label ── */
    .video-label { font-size: 0.82em; color: #374151; margin-bottom: 5px; font-weight: 600; }

    /* ── Sidebar internals ── */
    .sb-logo {
        font-size: 1.1em;
        font-weight: 900;
        color: #111827;
        padding: 16px 16px 12px 16px;
        letter-spacing: -0.2px;
    }
    .sb-logo span { color: #2563eb; }
    .sb-section {
        font-size: 0.67em;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.3px;
        color: #9ca3af;
        padding: 0 16px;
        margin: 12px 0 4px 0;
    }
    .sb-stat-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 16px;
        font-size: 0.83em;
        color: #374151;
    }
    .sb-stat-val { font-weight: 700; color: #111827; }
    .sb-coming-soon {
        padding: 7px 12px;
        margin: 3px 8px;
        border: 1px dashed #d1d5db;
        border-radius: 4px;
        font-size: 0.82em;
        color: #9ca3af;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .cs-badge {
        background: #f3f4f6;
        border: 1px solid #e5e7eb;
        color: #9ca3af;
        font-size: 0.65em;
        font-weight: 700;
        padding: 1px 5px;
        border-radius: 2px;
        letter-spacing: 0.5px;
    }
    .sb-divider { border: none; border-top: 1px solid #f3f4f6; margin: 10px 0; }
    .sb-footer  { padding: 0 16px; font-size: 0.72em; color: #9ca3af; line-height: 1.6; }

    /* ── Daily numbers ── */
    .num-red    { color: #dc2626; font-size: 2em; font-weight: 900; }
    .num-yellow { color: #d97706; font-size: 2em; font-weight: 900; }
    .num-green  { color: #059669; font-size: 2em; font-weight: 900; }

    /* ── Streamlit overrides ── */
    div[data-testid="stProgress"] > div { border-radius: 2px !important; }
    .stButton > button                  { border-radius: 4px !important; }
    .stTextInput > div > div > input    { border-radius: 4px !important; }
    .stSelectbox > div > div            { border-radius: 4px !important; }
    div[data-testid="stAlert"]          { border-radius: 4px !important; }
    p, li, label, .stMarkdown           { color: #374151 !important; }
    div[data-testid="stCaption"]        { color: #6b7280 !important; }
    h1, h2, h3, h4 { color: #111827 !important; font-weight: 700 !important; }

    /* Hide default Streamlit header */
    #MainMenu, footer, header { visibility: hidden !important; }
</style>
"""


def render_topnav(username, cookie_manager=None):
    """Render the Khan Academy-style dark top navigation bar."""
    import streamlit as st

    col_nav, col_logout = st.columns([11, 1])
    with col_nav:
        st.markdown(f"""
            <div class="ka-nav">
                <div class="ka-logo-wrap">
                    <div class="ka-logo-icon">🧮</div>
                    <div class="ka-logo-text">Super<span>Maths</span></div>
                </div>
                <div class="ka-user">
                    <span>Hey, <strong style="color:#e5e7eb">{username}</strong></span>
                    <span class="ka-user-badge">STUDENT</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col_logout:
        st.write("")
        st.write("")
        if cookie_manager is not None:
            if st.button("Log Out", use_container_width=True):
                try:
                    if cookie_manager.get("supermaths_user"):
                        cookie_manager.delete("supermaths_user")
                except Exception:
                    pass
                for k in ["logged_in", "username", "active_assignment", "show_baseline",
                          "show_level_test", "practice_topic", "practice_grade"]:
                    st.session_state.pop(k, None)
                st.session_state.show_landing = True
                st.rerun()


def render_sidebar(p=None):
    """Render the persistent sidebar with stats and coming-soon modules."""
    import streamlit as st
    from datetime import date

    with st.sidebar:
        st.markdown(
            '<div class="sb-logo">🧮 Super<span>Maths</span></div>',
            unsafe_allow_html=True
        )
        st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

        if p is not None:
            today          = str(date.today())
            daily_answered = p.get("daily_answered", 0) if p.get("daily_date") == today else 0
            daily_correct  = p.get("daily_correct",  0) if p.get("daily_date") == today else 0
            overall_acc    = (
                int(p["total_correct"] / p["total_answered"] * 100)
                if p.get("total_answered", 0) > 0 else 0
            )
            daily_acc = int(daily_correct / daily_answered * 100) if daily_answered > 0 else 0

            st.markdown('<div class="sb-section">Quick Stats</div>', unsafe_allow_html=True)
            stats = [
                ("Grade",             f"Grade {p.get('grade', '—')}"),
                ("Level",             f"Level {p.get('level', '—')}"),
                ("Total Questions",   str(p.get("total_answered", 0))),
                ("Overall Accuracy",  f"{overall_acc}%"),
                ("Today's Questions", str(daily_answered)),
                ("Today's Accuracy",  f"{daily_acc}%" if daily_answered else "—"),
            ]
            for label, value in stats:
                st.markdown(f"""
                    <div class="sb-stat-row">
                        <span>{label}</span>
                        <span class="sb-stat-val">{value}</span>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="sb-section">Quick Stats</div>', unsafe_allow_html=True)
            st.markdown(
                '<div style="padding:6px 16px;font-size:0.80em;color:#9ca3af;">'
                'Complete placement test to see your stats.</div>',
                unsafe_allow_html=True
            )

        st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
        st.markdown('<div class="sb-section">Coming Soon</div>', unsafe_allow_html=True)
        for module, icon in [("Geometry", "📐"), ("AP Prep", "📗"), ("SAT Prep", "✏️")]:
            st.markdown(f"""
                <div class="sb-coming-soon">
                    <span>{icon} {module}</span>
                    <span class="cs-badge">SOON</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
        st.markdown(
            '<div class="sb-footer">Free to use · Grades 1–12<br>Powered by AI</div>',
            unsafe_allow_html=True
        )
