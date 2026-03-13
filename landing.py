import streamlit as st

def show_landing():
    st.markdown("""
        <style>
            body, .stApp {
                background: #f0f2f5 !important;
                color: #1a1a2e !important;
            }
            section[data-testid="stSidebar"] { display: none !important; }

            .landing-hero {
                text-align: center;
                padding: 64px 20px 36px 20px;
            }
            .landing-title {
                font-size: 3.2em;
                font-weight: 900;
                color: #111827;
                margin-bottom: 10px;
                letter-spacing: -1px;
            }
            .landing-accent {
                color: #2563eb;
            }
            .landing-subtitle {
                font-size: 1.15em;
                color: #6b7280;
                margin-bottom: 36px;
                line-height: 1.6;
            }
            .feature-card {
                background: #ffffff;
                border: 1px solid #d1d5db;
                border-top: 4px solid #2563eb;
                border-radius: 4px;
                padding: 26px 20px;
                text-align: center;
                height: 100%;
            }
            .feature-icon  { font-size: 2em; margin-bottom: 10px; }
            .feature-title { font-size: 1em; font-weight: 700; color: #111827; margin-bottom: 6px; }
            .feature-desc  { font-size: 0.88em; color: #6b7280; line-height: 1.55; }
            .footer-text   { text-align: center; color: #9ca3af; font-size: 0.82em; padding: 28px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="landing-hero">
            <div class="landing-title">🧮 Super<span class="landing-accent">Maths</span></div>
            <div class="landing-subtitle">
                Your personal AI maths tutor.<br>
                Learn at your own pace — level up as you go.
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    features = [
        ("🎯", "Personalised Learning",   "Start with a placement test and get questions tailored to your exact level."),
        ("🤖", "AI-Generated Questions",  "Every question is freshly generated — no repeats, infinite practice."),
        ("💡", "Instant Hints",           "Stuck? Get a step-by-step explanation from an AI tutor on demand."),
        ("💵", "Completely Free",         "Free and open source — built to help students with maths, no strings attached."),
    ]
    for col, (icon, title, desc) in zip([col1, col2, col3, col4], features):
        with col:
            st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-desc">{desc}</div>
                </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col_a, col_b, col_c = st.columns([1.5, 1, 1.5])
    with col_b:
        if st.button("Get Started →", use_container_width=True, type="primary"):
            st.session_state.show_landing = False
            st.rerun()

    st.markdown(
        '<div class="footer-text">Free to use &nbsp;·&nbsp; Grades 1–12 &nbsp;·&nbsp; Powered by AI</div>',
        unsafe_allow_html=True
    )
