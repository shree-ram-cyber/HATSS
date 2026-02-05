import streamlit as st
import random
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Security Control", layout="wide")

# -----------------------------
# GLOBAL STYLE — CONTROL ROOM
# -----------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #0b1220;
    color: #e5e7eb;
}

.panel {
    background: #111827;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #1f2937;
    box-shadow: 0 0 12px rgba(0,0,0,0.4);
}

.title {
    font-size: 30px;
    font-weight: 700;
}

.metric-big {
    font-size: 28px;
    font-weight: bold;
}

.green {color:#22c55e;}
.red {color:#ef4444;}
.yellow {color:#f59e0b;}

.alert {
    background:#2a0d0d;
    border:1px solid #ef4444;
    padding:20px;
    border-radius:14px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "known" not in st.session_state:
    st.session_state.known = 18

if "unknown" not in st.session_state:
    st.session_state.unknown = 5

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🔐 Security Panel")

st.session_state.page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Alert Center", "Memory Logs", "Settings"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("System Status:")
st.sidebar.markdown("<span class='green'>● ACTIVE</span>",
                    unsafe_allow_html=True)

# =========================================================
# DASHBOARD
# =========================================================
if st.session_state.page == "Dashboard":

    st.markdown("<div class='title'>🏠 Live Security Dashboard</div>",
                unsafe_allow_html=True)

    left, right = st.columns([2,1])

    # ---- Camera Panel ----
    with left:
        st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.subheader("Live Camera Feed")

        st.info("Camera preview placeholder")

        st.markdown("</div>", unsafe_allow_html=True)

    # ---- Metrics Panel ----
    with right:
        st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.subheader("System Metrics")

        st.markdown(
            f"<div class='metric-big green'>{st.session_state.known}</div> Known Profiles",
            unsafe_allow_html=True)

        st.markdown(
            f"<div class='metric-big red'>{st.session_state.unknown}</div> Intruder Records",
            unsafe_allow_html=True)

        st.markdown(
            f"<div class='metric-big yellow'>{random.randint(1,5)} sec</div> Last Scan",
            unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    if st.button("🔍 Simulate Detection"):
        if random.choice([True, False]):
            st.session_state.page = "Alert Center"
            st.rerun()
        else:
            st.success("Authorized individual — no threat detected")

# =========================================================
# ALERT CENTER
# =========================================================
elif st.session_state.page == "Alert Center":

    st.markdown("<div class='title red'>🚨 Intrusion Alert</div>",
                unsafe_allow_html=True)

    st.markdown("<div class='alert'>", unsafe_allow_html=True)

    st.error("Unauthorized presence detected")

    col1, col2 = st.columns(2)

    with col1:
        st.warning("Captured image placeholder")

    with col2:
        score = round(random.uniform(0.30,0.55),2)
        st.write(f"Similarity Score: **{score}**")
        st.write("Threat Level: **HIGH**")

        st.divider()

        if st.button("✅ Approve"):
            st.session_state.known += 1
            st.success("Added to authorized memory")
            time.sleep(1)
            st.session_state.page = "Dashboard"
            st.rerun()

        if st.button("❌ Reject"):
            st.session_state.unknown += 1
            st.warning("Intruder recorded")
            time.sleep(1)
            st.session_state.page = "Dashboard"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MEMORY LOGS
# =========================================================
elif st.session_state.page == "Memory Logs":

    st.markdown("<div class='title'>🧠 Memory Logs</div>",
                unsafe_allow_html=True)

    st.subheader("Authorized Profiles")

    cols = st.columns(6)
    for i in range(12):
        with cols[i % 6]:
            st.info("KNOWN")

    st.divider()

    st.subheader("Intruder Records")

    cols = st.columns(6)
    for i in range(8):
        with cols[i % 6]:
            st.error("UNKNOWN")

# =========================================================
# SETTINGS
# =========================================================
elif st.session_state.page == "Settings":

    st.markdown("<div class='title'>⚙ System Settings</div>",
                unsafe_allow_html=True)

    st.markdown("<div class='panel'>", unsafe_allow_html=True)

    st.slider("Detection Sensitivity", 1, 10, 6)

    st.checkbox("Push Alerts", True)
    st.checkbox("Alarm Sound", True)

    if st.button("Clear Intruder Logs"):
        st.session_state.unknown = 0
        st.success("Intruder logs cleared")

    st.markdown("</div>", unsafe_allow_html=True)
