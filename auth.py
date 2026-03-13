import streamlit as st
from database import create_user, login_user

def get_client_info():
    try:
        headers = st.context.headers
        ua = headers.get("User-Agent", "Unknown")
        ip = headers.get("X-Forwarded-For", headers.get("Host", "Unknown"))
        return ip, ua
    except Exception:
        return "Unknown", "Unknown"

def show_auth(cookie_manager):
    st.markdown("""
        <style>
            body, .stApp {
                background: #f0f2f5 !important;
                color: #1a1a2e !important;
            }
            section[data-testid="stSidebar"] { display: none !important; }
            .auth-card {
                background: #ffffff;
                border: 1px solid #d1d5db;
                border-top: 4px solid #2563eb;
                border-radius: 4px;
                padding: 36px 32px 32px 32px;
            }
            .auth-title {
                font-size: 1.6em;
                font-weight: 900;
                color: #111827;
                margin-bottom: 4px;
            }
            .auth-sub {
                font-size: 0.9em;
                color: #6b7280;
                margin-bottom: 24px;
            }
            p, label, .stMarkdown { color: #374151 !important; }
        </style>
    """, unsafe_allow_html=True)

    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown("""
            <div class="auth-card">
                <div class="auth-title">🧮 SuperMaths</div>
                <div class="auth-sub">Welcome back — let's get learning.</div>
            </div>
        """, unsafe_allow_html=True)
        st.write("")

        tab1, tab2 = st.tabs(["  Log In  ", "  Sign Up  "])

        with tab1:
            username    = st.text_input("Username", key="login_username",    placeholder="Your username")
            password    = st.text_input("Password", type="password", key="login_password", placeholder="Your password")
            remember_me = st.checkbox("Keep me logged in", value=True)

            if st.button("Log In", use_container_width=True, type="primary"):
                if username and password:
                    if login_user(username, password):
                        st.session_state.logged_in = True
                        st.session_state.username  = username
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
            new_password     = st.text_input("Password",         type="password", key="signup_password",  placeholder="Choose a password")
            confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password", placeholder="Repeat your password")

            if st.button("Create Account", use_container_width=True, type="primary"):
                if new_username and new_password and confirm_password:
                    if new_password != confirm_password:
                        st.error("Passwords don't match.")
                    else:
                        ip, ua = get_client_info()
                        success, message = create_user(new_username, new_password, ip, ua)
                        if success:
                            st.success("Account created! Head over to Log In.")
                        else:
                            st.error(message)
                else:
                    st.warning("Please fill in all fields.")
