import streamlit as st
import datetime

LOG_FILE = "safe_keylog.txt"

st.title("🔐 Safe Key Logger Simulation (Streamlit)")
st.write("This only logs keys typed inside this app — not your computer.")

# Initialize session state
if "log" not in st.session_state:
    st.session_state.log = []

text = st.text_input("Type something here:")

if text:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {text}"
    st.session_state.log.append(entry)

    # Save to file
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")

st.subheader("📌 Logged Keys")
for line in st.session_state.log:
    st.write(line)

# Clear button
if st.button("Clear Log"):
    st.session_state.log = []
    open(LOG_FILE, "w").close()
    st.success("Log cleared!")
