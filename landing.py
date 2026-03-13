import streamlit as st

def show_landing():
    st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
*,*::before,*::after{box-sizing:border-box;}
html,body,.stApp,.stApp>div,.main,.main>div,
.block-container,[data-testid="stAppViewBlockContainer"]{
    padding-top:0!important;margin-top:0!important;
    background:#f4f6f9!important;color:#1d2129!important;
    font-family:'Nunito','Segoe UI',sans-serif!important;
}
section[data-testid="stSidebar"]{display:none!important;}
#MainMenu,footer,[data-testid="stHeader"],[data-testid="stToolbar"],
[data-testid="stDecoration"],[data-testid="stStatusWidget"]{
    display:none!important;visibility:hidden!important;height:0!important;
}
.land-bar{
    background:#1a1f2e;height:62px;
    display:flex;align-items:center;padding:0 36px;
    border-bottom:3px solid #1a73e8;
    margin-left:-1rem;margin-right:-1rem;
}
.land-logo{font-family:'Nunito',sans-serif;font-size:1.3em;font-weight:900;color:#fff;}
.land-logo span{color:#74b9ff;}
.hero{
    background:#fff;border-bottom:1px solid #dde2ea;
    padding:72px 40px 60px;text-align:center;
}
.hero-eyebrow{
    font-size:0.78em;font-weight:800;letter-spacing:2.5px;
    text-transform:uppercase;color:#1a73e8;margin-bottom:16px;
}
.hero-title{
    font-family:'Nunito',sans-serif;font-size:3.2em;font-weight:900;
    color:#1d2129;margin-bottom:16px;line-height:1.1;letter-spacing:-1px;
}
.hero-accent{color:#1a73e8;}
.hero-sub{
    font-size:1.1em;color:#6b7480;line-height:1.7;
    max-width:500px;margin:0 auto;
}
.feature-card{
    background:#fff;border:1px solid #dde2ea;border-top:3px solid #1a73e8;
    border-radius:4px;padding:28px 20px;text-align:center;height:100%;
}
.feature-icon{font-size:2.2em;margin-bottom:12px;}
.feature-title{font-family:'Nunito',sans-serif;font-size:1.05em;font-weight:800;color:#1d2129;margin-bottom:8px;}
.feature-desc{font-size:0.88em;color:#6b7480;line-height:1.6;}
.land-footer{
    text-align:center;color:#9ba5b7;font-size:0.82em;
    padding:32px;border-top:1px solid #e2e7f0;font-family:'Nunito',sans-serif;
}
.stButton>button{
    font-family:'Nunito',sans-serif!important;font-weight:800!important;
    font-size:1.05em!important;border-radius:4px!important;min-height:50px!important;
}
.stButton>button[kind="primary"]{
    background:#1a73e8!important;color:#fff!important;border:none!important;
    box-shadow:0 2px 8px rgba(26,115,232,0.35)!important;
}
.stButton>button[kind="primary"]:hover{background:#1558b0!important;}
p,li,label,.stMarkdown{color:#374151!important;}
h1,h2,h3,h4{font-family:'Nunito',sans-serif!important;color:#1d2129!important;font-weight:800!important;}
</style>""", unsafe_allow_html=True)

    st.markdown("""
<div class="land-bar">
  <div class="land-logo">🧮 Super<span>Maths</span></div>
</div>
<div class="hero">
  <div class="hero-eyebrow">Free · AI-Powered · Grades 1–12</div>
  <div class="hero-title">Your personal<br><span class="hero-accent">maths tutor.</span></div>
  <div class="hero-sub">Learn at your own pace — placement-tested, level-based,<br>and completely free for every student.</div>
</div>""", unsafe_allow_html=True)

    st.write("")
    col1, col2, col3, col4 = st.columns(4)
    features = [
        ("🎯", "Personalised",    "Placement test places you at exactly the right level from day one."),
        ("🤖", "AI Questions",    "Every question freshly generated — no two sessions the same."),
        ("💡", "Instant Hints",   "Stuck? Get a clear step-by-step walkthrough on demand."),
        ("🆓", "Completely Free", "No ads, no subscriptions. Built for every student, everywhere."),
    ]
    for col, (icon, title, desc) in zip([col1, col2, col3, col4], features):
        with col:
            st.markdown(f"""<div class="feature-card">
  <div class="feature-icon">{icon}</div>
  <div class="feature-title">{title}</div>
  <div class="feature-desc">{desc}</div>
</div>""", unsafe_allow_html=True)

    st.write("")
    st.write("")
    _, col_b, _ = st.columns([1.5, 1, 1.5])
    with col_b:
        if st.button("Get Started →", use_container_width=True, type="primary"):
            st.session_state.show_landing = False
            st.rerun()

    st.markdown('<div class="land-footer">Free to use &nbsp;·&nbsp; Grades 1–12 &nbsp;·&nbsp; Powered by AI</div>', unsafe_allow_html=True)
