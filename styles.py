# SuperMaths Design System v1.3

GLOBAL_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&display=swap');

*,*::before,*::after{box-sizing:border-box;}

html,body,.stApp{
    background:#f4f6f9!important;
    color:#1d2129!important;
    font-family:'Nunito','Segoe UI',sans-serif!important;
}

/* ── Kill every gap above the navbar ── */
.stApp,.stApp>div,.main,.main>div,
.block-container,[data-testid="stAppViewBlockContainer"],
[data-testid="stVerticalBlock"]>div:first-child{
    padding-top:0!important;margin-top:0!important;
}
.main .block-container{
    padding-left:2rem!important;padding-right:2rem!important;
    max-width:1180px!important;
}
#MainMenu,footer,[data-testid="stHeader"],
[data-testid="stToolbar"],[data-testid="stDecoration"],
[data-testid="stStatusWidget"]{
    display:none!important;visibility:hidden!important;height:0!important;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"]{
    background:#ffffff!important;
    border-right:1px solid #dde2ea!important;
    min-width:256px!important;max-width:256px!important;
    transform:none!important;visibility:visible!important;display:block!important;
}
section[data-testid="stSidebar"][aria-expanded="false"]{
    margin-left:0!important;transform:translateX(0)!important;
}
button[data-testid="stSidebarNavCollapseButton"],
button[data-testid="collapsedControl"],
button[data-testid="stSidebarCollapseButton"],
[data-testid="stSidebarCollapseButton"],
[data-testid="collapsedControl"],
button[title="Collapse sidebar"],button[title="Expand sidebar"],
button[aria-label="Collapse sidebar"],button[aria-label="Expand sidebar"],
section[data-testid="stSidebar"] button[kind="header"]{
    display:none!important;visibility:hidden!important;pointer-events:none!important;
}

/* ── Navbar ── */
.ka-nav{
    background:#1a1f2e;
    height:62px;padding:0 32px;
    display:flex;align-items:center;justify-content:space-between;
    border-bottom:3px solid #1a73e8;
    margin-top:-1px;margin-left:-2rem;margin-right:-2rem;margin-bottom:24px;
    position:relative;z-index:100;
}
.ka-logo-wrap{display:flex;align-items:center;gap:12px;}
.ka-logo-icon{
    width:36px;height:36px;background:#1a73e8;border-radius:4px;
    display:flex;align-items:center;justify-content:center;font-size:1.15em;
}
.ka-logo-text{
    font-family:'Nunito',sans-serif;font-size:1.3em;font-weight:900;color:#fff;
}
.ka-logo-text span{color:#74b9ff;}
.ka-user{display:flex;align-items:center;gap:14px;font-size:0.9em;color:#9ba5b7;}
.ka-user strong{color:#e8ecf4;}
.ka-badge{
    background:#1a73e8;color:#fff;font-size:0.72em;font-weight:800;
    padding:3px 10px;border-radius:3px;letter-spacing:0.6px;text-transform:uppercase;
    font-family:'Nunito',sans-serif;
}

/* ── Buttons — squared, Nunito, readable ── */
.stButton>button{
    font-family:'Nunito',sans-serif!important;
    font-weight:700!important;font-size:1em!important;
    border-radius:4px!important;min-height:46px!important;
    padding:0 22px!important;
    transition:all 0.12s ease!important;
    letter-spacing:0.2px!important;
}
.stButton>button:not([kind="primary"]){
    background:#ffffff!important;color:#1d2129!important;
    border:1.5px solid #c4cad4!important;
}
.stButton>button:not([kind="primary"]):hover{
    background:#eef2ff!important;border-color:#1a73e8!important;color:#1a73e8!important;
}
.stButton>button[kind="primary"]{
    background:#1a73e8!important;color:#ffffff!important;
    border:none!important;font-weight:800!important;
    box-shadow:0 2px 6px rgba(26,115,232,0.35)!important;
}
.stButton>button[kind="primary"]:hover{
    background:#1558b0!important;box-shadow:0 4px 14px rgba(26,115,232,0.45)!important;
    transform:translateY(-1px)!important;
}

/* ── Inputs ── */
.stTextInput>div>div>input{
    border-radius:4px!important;border:1.5px solid #c4cad4!important;
    min-height:44px!important;font-size:0.96em!important;
    padding:0 13px!important;background:#fff!important;color:#1d2129!important;
    font-family:'Nunito',sans-serif!important;
}
.stTextInput>div>div>input:focus{
    border-color:#1a73e8!important;
    box-shadow:0 0 0 3px rgba(26,115,232,0.12)!important;outline:none!important;
}
.stTextInput label{
    color:#374151!important;font-weight:700!important;
    font-family:'Nunito',sans-serif!important;
}
.stSelectbox>div>div{border-radius:4px!important;min-height:44px!important;}

/* ── Radio (answer options) ── */
div[data-testid="stRadio"] label{
    font-family:'Nunito',sans-serif!important;font-weight:600!important;
    color:#374151!important;margin-bottom:5px!important;
}
div[data-testid="stRadio"]>div{gap:6px!important;display:flex!important;flex-direction:column!important;}
div[data-testid="stRadio"]>div>label{
    background:#fff!important;border:1.5px solid #d8dde6!important;
    border-radius:4px!important;padding:13px 16px!important;
    cursor:pointer!important;min-height:50px!important;
    display:flex!important;align-items:center!important;
    font-size:0.97em!important;color:#1d2129!important;
    transition:border-color 0.12s,background 0.12s!important;width:100%!important;
}
div[data-testid="stRadio"]>div>label:hover{
    border-color:#1a73e8!important;background:#eef4fd!important;
}

/* ── Progress bar (Streamlit native) ── */
div[data-testid="stProgress"]>div{
    border-radius:2px!important;height:8px!important;background:#e2e7f0!important;
}
div[data-testid="stProgress"]>div>div{
    background:#1a73e8!important;border-radius:2px!important;
}

/* ── Daily goals progress bar ── */
.daily-bar-wrap{
    background:#fff;border:1px solid #dde2ea;border-radius:4px;
    padding:16px 20px;margin-bottom:20px;
}
.daily-bar-label{
    display:flex;justify-content:space-between;align-items:baseline;
    margin-bottom:10px;
}
.daily-bar-title{
    font-family:'Nunito',sans-serif;font-weight:800;font-size:0.95em;color:#1d2129;
}
.daily-bar-count{
    font-family:'Nunito',sans-serif;font-weight:700;font-size:0.88em;color:#6b7480;
}
.daily-bar-track{
    width:100%;height:14px;background:#e8ecf2;border-radius:3px;overflow:hidden;
    position:relative;
}
.daily-bar-fill{
    height:100%;border-radius:3px;
    transition:width 0.5s ease, background 0.5s ease;
    position:relative;
}
.daily-bar-milestones{
    display:flex;justify-content:space-between;margin-top:6px;
}
.daily-bar-ms{font-size:0.7em;color:#9ba5b7;font-family:'Nunito',sans-serif;}

/* ── Stat cards ── */
.stat-card{
    background:#fff;border:1px solid #dde2ea;
    border-top:3px solid #1a73e8;border-radius:4px;
    padding:20px 16px;text-align:center;
}
.stat-label{
    font-size:0.68em;color:#6b7480;text-transform:uppercase;
    letter-spacing:1.2px;font-weight:700;font-family:'Nunito',sans-serif;
}
.stat-value{font-size:2em;font-weight:800;margin:6px 0 2px 0;color:#1d2129;font-family:'Nunito',sans-serif;}
.stat-green{color:#0f7b45;}.stat-purple{color:#6d3fc7;}
.stat-blue{color:#1a73e8;}.stat-dark{color:#1d2129;}

/* ── Section titles ── */
.section-title{
    font-family:'Nunito',sans-serif;font-size:1.05em;font-weight:800;
    color:#1d2129;margin:28px 0 12px 0;padding-bottom:9px;
    border-bottom:2px solid #e2e7f0;display:flex;align-items:center;gap:8px;
}

/* ── Topic rows ── */
.topic-row{
    background:#fff;border:1px solid #dde2ea;border-left:4px solid #1a73e8;
    border-radius:4px;padding:14px 18px;margin-bottom:9px;
}
.topic-row-complete{border-left-color:#0f7b45!important;background:#f3faf6!important;}
.topic-row strong{color:#1d2129!important;font-size:0.97em;font-family:'Nunito',sans-serif;}

/* ── Quiz pills ── */
.quiz-pill{
    display:inline-block;padding:3px 11px;border-radius:3px;
    font-size:0.75em;margin-right:6px;font-weight:700;font-family:'Nunito',sans-serif;
}
.pill-done{background:#d4edda;color:#155724;border:1px solid #b2dfb7;}
.pill-todo{background:#f0f1f4;color:#6b7480;border:1px solid #dde2ea;}

/* ── Badge grid — MEDALS (compact) ── */
.badge-grid{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:12px;}
.badge-card{
    width:66px;
    display:flex;flex-direction:column;align-items:center;
    text-align:center;cursor:default;
    transition:transform 0.15s;
    flex-shrink:0;position:relative;
}
.badge-card:hover{transform:translateY(-2px);}
/* Ribbon */
.badge-ribbon{
    width:16px;height:14px;
    background:linear-gradient(180deg,#b8bfc9 0%,#8e97a3 100%);
    border-radius:2px 2px 0 0;
    position:relative;z-index:1;
}
.badge-ribbon::after{
    content:'';position:absolute;bottom:-4px;left:50%;transform:translateX(-50%);
    width:0;height:0;
    border-left:8px solid transparent;border-right:8px solid transparent;
    border-top:5px solid #8e97a3;
}
/* Medal disc */
.badge-disc{
    width:60px;height:60px;border-radius:50%;
    background:linear-gradient(135deg,#c8cdd6 0%,#9aa0ad 50%,#b0b6c0 100%);
    border:2.5px solid #8e97a3;
    box-shadow:0 2px 8px rgba(0,0,0,0.15),inset 0 1px 2px rgba(255,255,255,0.4);
    display:flex;flex-direction:column;align-items:center;justify-content:center;
    padding:4px 3px;gap:1px;
    position:relative;z-index:2;
    margin-top:4px;
}
/* Earned — gold */
.badge-card-earned .badge-ribbon{
    background:linear-gradient(180deg,#fde68a 0%,#d4a017 100%);
}
.badge-card-earned .badge-ribbon::after{border-top-color:#d4a017;}
.badge-card-earned .badge-disc{
    background:linear-gradient(135deg,#fef3c7 0%,#fbbf24 35%,#d97706 70%,#f59e0b 100%);
    border-color:#c47f17;
    box-shadow:0 3px 12px rgba(245,158,11,0.45),inset 0 1px 2px rgba(255,255,255,0.5);
}
.badge-icon{font-size:1.35em;line-height:1;filter:drop-shadow(0 1px 1px rgba(0,0,0,0.15));}
.badge-name{
    font-size:0.52em;font-weight:800;color:#1d2129;
    line-height:1.2;font-family:'Nunito',sans-serif;
    max-width:62px;word-break:break-word;
    margin-top:2px;text-align:center;
}
.badge-locked{opacity:0.38;filter:grayscale(75%);}

/* ── Sidebar recent badges ── */
.sb-badge-row{
    display:flex;align-items:center;gap:8px;
    padding:5px 18px;font-size:0.82em;color:#374151;
    font-family:'Nunito',sans-serif;border-radius:3px;margin:1px 6px;
}
.sb-badge-row:hover{background:#f7f8fa;}
.sb-badge-icon{font-size:1.1em;min-width:20px;text-align:center;}
.sb-badge-name{font-weight:700;color:#1d2129;font-size:0.9em;}
.sb-badge-desc{font-size:0.78em;color:#6b7480;line-height:1.3;}

/* ── Level test banner ── */
.lt-banner{
    background:#eef4fd;border:1px solid #b3ccf0;border-left:4px solid #1a73e8;
    border-radius:4px;padding:15px 20px;margin:16px 0;
    color:#0d2d5e;font-size:0.95em;font-family:'Nunito',sans-serif;
}

/* ── Practice session history ── */
.session-history{
    background:#fff;border:1px solid #dde2ea;border-radius:4px;
    overflow:hidden;margin-top:12px;
}
.session-row{
    display:flex;align-items:center;gap:12px;
    padding:10px 16px;border-bottom:1px solid #f0f2f6;
    font-family:'Nunito',sans-serif;font-size:0.9em;
}
.session-row:last-child{border-bottom:none;}
.session-num{font-weight:800;color:#1a73e8;min-width:26px;}
.session-score{font-weight:700;color:#1d2129;}
.session-acc-bar{flex:1;height:8px;background:#e8ecf2;border-radius:2px;overflow:hidden;}
.session-acc-fill{height:100%;border-radius:2px;}
.session-acc-label{font-weight:700;min-width:40px;text-align:right;}

/* ── Video label ── */
.video-label{font-size:0.84em;color:#374151;margin-bottom:5px;font-weight:700;font-family:'Nunito',sans-serif;}

/* ── Sidebar internals ── */
.sb-logo{
    font-family:'Nunito',sans-serif;font-size:1.15em;font-weight:900;
    color:#1d2129;padding:20px 18px 14px 18px;
}
.sb-logo span{color:#1a73e8;}
.sb-section{
    font-size:0.65em;font-weight:800;text-transform:uppercase;
    letter-spacing:1.4px;color:#9ba5b7;padding:0 18px;margin:14px 0 5px 0;
    font-family:'Nunito',sans-serif;
}
.sb-stat-row{
    display:flex;justify-content:space-between;align-items:center;
    padding:6px 18px;font-size:0.86em;color:#4b5563;border-radius:3px;margin:1px 6px;
    font-family:'Nunito',sans-serif;
}
.sb-stat-row:hover{background:#f7f8fa;}
.sb-stat-val{font-weight:800;color:#1d2129;}
.sb-coming-soon{
    padding:9px 14px;margin:4px 10px;border:1px dashed #dde2ea;border-radius:4px;
    font-size:0.83em;color:#9ba5b7;display:flex;justify-content:space-between;align-items:center;
    font-family:'Nunito',sans-serif;
}
.cs-badge{
    background:#f0f1f4;border:1px solid #dde2ea;color:#9ba5b7;
    font-size:0.64em;font-weight:800;padding:2px 6px;border-radius:3px;letter-spacing:0.5px;
}
.sb-divider{border:none;border-top:1px solid #eef0f5;margin:10px 0;}
.sb-footer{padding:0 18px;font-size:0.73em;color:#9ba5b7;line-height:1.7;font-family:'Nunito',sans-serif;}

/* ── Daily number colours ── */
.num-red{color:#c0392b;font-size:2.1em;font-weight:800;font-family:'Nunito',sans-serif;}
.num-yellow{color:#c87a00;font-size:2.1em;font-weight:800;font-family:'Nunito',sans-serif;}
.num-green{color:#0f7b45;font-size:2.1em;font-weight:800;font-family:'Nunito',sans-serif;}

/* ── Alerts ── */
div[data-testid="stAlert"]{border-radius:4px!important;}
div[data-testid="stAlert"] p{color:#1d2129!important;}

/* ── Typography ── */
h1,h2,h3,h4{
    font-family:'Nunito',sans-serif!important;color:#1d2129!important;font-weight:800!important;
}
h1{font-size:2em!important;}h2{font-size:1.55em!important;}h3{font-size:1.25em!important;}
p,li,.stMarkdown p{color:#374151!important;}
label{color:#374151!important;font-weight:600!important;font-family:'Nunito',sans-serif!important;}
div[data-testid="stCaption"]{color:#6b7480!important;}
.stTabs [data-baseweb="tab"]{
    font-family:'Nunito',sans-serif!important;font-weight:700!important;font-size:0.95em!important;
}
hr{border-color:#e2e7f0!important;}
div[data-testid="stSpinner"] p{color:#6b7480!important;}
</style>"""


def _daily_progress_bar(daily_answered: int) -> str:
    """Return HTML for the daily question progress bar (red → yellow → gold gradient)."""
    goal = 30
    pct  = min(100, int(daily_answered / goal * 100))

    remaining = max(0, goal - daily_answered)
    label = (
        f"{daily_answered}/{goal} questions today"
        if daily_answered < goal
        else f"🎉 Daily goal smashed! ({daily_answered} questions)"
    )
    sub = "" if daily_answered >= goal else f"{remaining} to go"

    milestones_html = ""
    for ms, lbl in [(0,"0"), (10,"10"), (20,"20"), (30,"30🎯")]:
        ms_pct = ms / goal * 100
        milestones_html += f'<span style="position:absolute;left:{ms_pct}%;transform:translateX(-50%);font-size:0.68em;color:#9ba5b7;font-family:Nunito,sans-serif;font-weight:700;">{lbl}</span>'

    return f"""
<div class="daily-bar-wrap">
  <div class="daily-bar-label">
    <span class="daily-bar-title">📅 Daily Progress</span>
    <span class="daily-bar-count">{label} {sub}</span>
  </div>
  <div class="daily-bar-track" style="position:relative;background:#e8ecf2;overflow:visible;">
    <!-- gradient track -->
    <div style="position:absolute;inset:0;border-radius:3px;
         background:linear-gradient(to right,#e53e3e 0%,#ed8936 30%,#ecc94b 60%,#d4a017 100%);
         overflow:hidden;">
      <!-- right mask to show only the filled portion -->
      <div style="position:absolute;top:0;right:0;height:100%;
           width:{100-pct}%;background:#e8ecf2;transition:width 0.5s ease;"></div>
    </div>
  </div>
  <div style="position:relative;height:18px;margin-top:2px;">
    {milestones_html}
  </div>
</div>"""


def render_topnav(username, cookie_manager=None):
    import streamlit as st

    st.markdown("""<style>
        .stApp,.stApp>div,.main,.main>div,
        .block-container,[data-testid="stAppViewBlockContainer"],
        [data-testid="stVerticalBlockBorderWrapper"],
        section.main>div{padding-top:0!important;margin-top:0!important;}
    </style>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="ka-nav">
      <div class="ka-logo-wrap">
        <div class="ka-logo-icon">🧮</div>
        <div class="ka-logo-text">Super<span>Maths</span></div>
      </div>
      <div class="ka-user">
        <span>Hey, <strong>{username}</strong></span>
        <span class="ka-badge">Student</span>
      </div>
    </div>""", unsafe_allow_html=True)

    if cookie_manager is not None:
        col_spacer, col_out = st.columns([20, 2])
        with col_out:
            if st.button("Log Out", use_container_width=True):
                try:
                    if cookie_manager.get("supermaths_user"):
                        cookie_manager.delete("supermaths_user")
                except Exception:
                    pass
                for k in ["logged_in","username","active_assignment",
                          "show_baseline","show_level_test","practice_topic","practice_grade"]:
                    st.session_state.pop(k, None)
                st.session_state.show_landing = True
                st.rerun()


def render_sidebar(p=None):
    import streamlit as st
    from datetime import date

    with st.sidebar:
        st.markdown('<div class="sb-logo">🧮 Super<span>Maths</span></div>', unsafe_allow_html=True)
        st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

        if p is not None:
            today = str(date.today())
            da    = p.get("daily_answered",0) if p.get("daily_date")==today else 0
            dc    = p.get("daily_correct",0)  if p.get("daily_date")==today else 0
            oa    = int(p["total_correct"]/p["total_answered"]*100) if p.get("total_answered",0)>0 else 0
            dac   = int(dc/da*100) if da>0 else 0
            streak= p.get("streak",0)

            st.markdown('<div class="sb-section">My Stats</div>', unsafe_allow_html=True)
            for lbl, val in [
                ("Grade",           f"Grade {p.get('grade','—')}"),
                ("Level",           f"Level {p.get('level','—')}"),
                ("🔥 Streak",       f"{streak} day{'s' if streak!=1 else ''}"),
                ("Total Answered",  str(p.get("total_answered",0))),
                ("Overall Acc.",    f"{oa}%"),
                ("Today's Qs",      str(da)),
                ("Today's Acc.",    f"{dac}%" if da else "—"),
            ]:
                st.markdown(f"""<div class="sb-stat-row">
                    <span>{lbl}</span><span class="sb-stat-val">{val}</span>
                </div>""", unsafe_allow_html=True)
        else:
            st.markdown('<div class="sb-section">My Stats</div>', unsafe_allow_html=True)
            st.markdown('<div style="padding:8px 18px;font-size:0.82em;color:#9ba5b7;">Complete placement test to see stats.</div>', unsafe_allow_html=True)

        from badges import BADGES as _BADGES
        earned_keys = p.get("badges", []) if p else []
        if earned_keys:
            st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
            st.markdown('<div class="sb-section">🏅 Unlocked Badges</div>', unsafe_allow_html=True)
            # Show most recently earned first (last in list = most recent)
            for key in reversed(earned_keys[-8:]):  # show up to 8
                b = _BADGES.get(key)
                if b:
                    st.markdown(f"""<div class="sb-badge-row">
                        <span class="sb-badge-icon">{b['icon']}</span>
                        <div>
                          <div class="sb-badge-name">{b['name']}</div>
                          <div class="sb-badge-desc">{b['desc']}</div>
                        </div>
                    </div>""", unsafe_allow_html=True)

        st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
        st.markdown('<div class="sb-section">Coming Soon</div>', unsafe_allow_html=True)
        for module, icon in [("Geometry","📐"),("AP Prep","📗"),("SAT Prep","✏️")]:
            st.markdown(f"""<div class="sb-coming-soon">
                <span>{icon} {module}</span><span class="cs-badge">SOON</span>
            </div>""", unsafe_allow_html=True)

        st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
        st.markdown('<div class="sb-footer">Free to use · Grades 1–12<br>Powered by AI</div>', unsafe_allow_html=True)
