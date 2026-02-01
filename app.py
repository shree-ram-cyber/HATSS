import streamlit as st
from PIL import Image
from main import run_detection

st.set_page_config(page_title="HATSS Test Panel")

st.title("HATSS – Face Recognition Test")

uploaded_file = st.file_uploader(
    "Upload an image to test",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    temp_path = "temp.jpg"
    image.save(temp_path)

    result = run_detection(temp_path)

    if result == "Known":
        st.success("✅ Known person detected")
    elif result == "Unknown":
        st.error("🚨 Unknown person detected – Alert triggered")
    else:
        st.warning(result)
