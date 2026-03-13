import streamlit as st
from database import create_user, login_user

def get_client_info():
    try:
        headers = st.context.headers
        ua = headers.get("User-Agent","Unknown")
        ip = headers.get("X-Forwarded-For", headers.get("Host","Unknown"))
        return ip, ua
    except Exception:
        return "Unknown","Unknown"

def show_auth(cookie_manager):
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
.auth-topbar{
    background:#1a1f2e;height:62px;
    display:flex;align-items:center;padding:0 36px;
    border-bottom:3px solid #1a73e8;
    margin-left:-1rem;margin-right:-1rem;margin-bottom:48px;
}
.auth-logo{font-family:'Nunito',sans-serif;font-size:1.3em;font-weight:900;color:#fff;}
.auth-logo span{color:#74b9ff;}
.auth-card{
    background:#fff;border:1px solid #dde2ea;border-top:4px solid #1a73e8;
    border-radius:4px;padding:36px 32px 32px;box-shadow:0 4px 20px rgba(0,0,0,0.06);
}
.auth-title{font-family:'Nunito',sans-serif;font-size:1.65em;font-weight:900;color:#1d2129;margin-bottom:4px;}
.auth-sub{font-size:0.92em;color:#6b7480;margin-bottom:24px;font-family:'Nunito',sans-serif;}
p,label,.stMarkdown{color:#374151!important;}
.stTextInput>div>div>input{
    border-radius:4px!important;border:1.5px solid #c4cad4!important;
    min-height:46px!important;font-size:0.96em!important;
    padding:0 14px!important;color:#1d2129!important;background:#fff!important;
    font-family:'Nunito',sans-serif!important;
}
.stTextInput>div>div>input:focus{
    border-color:#1a73e8!important;box-shadow:0 0 0 3px rgba(26,115,232,0.12)!important;
}
.stTextInput label{font-weight:700!important;color:#374151!important;font-family:'Nunito',sans-serif!important;}
.stButton>button{
    font-family:'Nunito',sans-serif!important;font-weight:800!important;
    font-size:0.97em!important;border-radius:4px!important;min-height:46px!important;
}
.stButton>button:not([kind="primary"]){
    background:#fff!important;color:#1d2129!important;border:1.5px solid #c4cad4!important;
}
.stButton>button:not([kind="primary"]):hover{background:#eef2ff!important;border-color:#1a73e8!important;}
.stButton>button[kind="primary"]{
    background:#1a73e8!important;color:#fff!important;border:none!important;
    box-shadow:0 2px 8px rgba(26,115,232,0.3)!important;
}
.stButton>button[kind="primary"]:hover{background:#1558b0!important;}
h1,h2,h3,h4{font-family:'Nunito',sans-serif!important;color:#1d2129!important;font-weight:800!important;}
.stTabs [data-baseweb="tab"]{font-family:'Nunito',sans-serif!important;font-weight:700!important;}
</style>""", unsafe_allow_html=True)

    st.markdown("""<div class="auth-topbar">
  <div class="auth-logo">🧮 Super<span>Maths</span></div>
</div>""", unsafe_allow_html=True)

    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("""<div class="auth-card">
  <div class="auth-title">Welcome back</div>
  <div class="auth-sub">Log in or create an account to continue.</div>
</div>""", unsafe_allow_html=True)
        st.write("")

        tab1, tab2 = st.tabs(["  Log In  ", "  Sign Up  "])

        with tab1:
            username    = st.text_input("Username", key="login_username", placeholder="Your username")
            password    = st.text_input("Password", type="password", key="login_password", placeholder="Your password")
            remember_me = st.checkbox("Keep me logged in", value=True)

            if st.button("Log In", use_container_width=True, type="primary"):
                if username and password:
                    if login_user(username, password):
                        st.session_state.logged_in    = True
                        st.session_state.username     = username
                        st.session_state.show_landing = False
                        if remember_me:
                            cookie_manager.set("supermaths_user", username, max_age=60*60*24*30)
                        st.rerun()
                    else:
                        st.error("Incorrect username or password.")
                else:
                    st.warning("Please fill in all fields.")

            st.write("")
            if st.button("← Back to Home", use_container_width=True):
                st.session_state.show_landing = True
                st.rerun()

        with tab2:
            new_username     = st.text_input("Username",         key="signup_username",  placeholder="Choose a username")
            new_password     = st.text_input("Password",         type="password", key="signup_password",  placeholder="At least 6 characters")
            confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password", placeholder="Repeat your password")

            if st.button("Create Account", use_container_width=True, type="primary"):
                if new_username and new_password and confirm_password:
                    if new_password != confirm_password:
                        st.error("Passwords don't match.")
                    elif len(new_password) < 6:
                        st.warning("Password must be at least 6 characters.")
                    else:
                        ip, ua = get_client_info()
                        success, message = create_user(new_username, new_password, ip, ua)
                        if success:
                            st.success("✅ Account created! Head over to Log In.")
                        else:
                            st.error(message)
                else:
                    st.warning("Please fill in all fields.")
