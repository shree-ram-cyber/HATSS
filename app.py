import streamlit as st
from PIL import Image
import os

from main import add_known_face, run_detection

st.set_page_config(page_title="HATSS", layout="centered")

st.title("🏠 HATSS – Smart Intrusion Detection")

# -------------------------------
# STEP 1: ADD KNOWN PERSON
# -------------------------------
st.header("Step 1: Add Known Person")

known_file = st.file_uploader(
    "Upload image of a trusted person",
    type=["jpg", "jpeg", "png"],
    key="known"
)

if known_file is not None:
    img = Image.open(known_file).convert("RGB")  # 🔥 FIX
    st.image(img, caption="Known Person", use_column_width=True)

    img.save("known_temp.jpg")
    success = add_known_face("known_temp.jpg")
    os.remove("known_temp.jpg")

    if success:
        st.success("✅ Known person added successfully")
    else:
        st.error("❌ No face detected. Try a clearer image.")

st.divider()

# -------------------------------
# STEP 2: DETECT INTRUSION
# -------------------------------
st.header("Step 2: Detect Person")

test_file = st.file_uploader(
    "Upload image to test",
    type=["jpg", "jpeg", "png"],
    key="test"
)

if test_file is not None:
    img = Image.open(test_file).convert("RGB")  # 🔥 FIX
    st.image(img, caption="Detected Person", use_column_width=True)

    img.save("test_temp.jpg")
    result = run_detection("test_temp.jpg")
    os.remove("test_temp.jpg")

    if result == "Known":
        st.success("✅ Known person – no alert sent")
    elif result == "Unknown":
        st.error("🚨 Unknown person detected – ALERT SENT")
    else:
        st.warning(result)
