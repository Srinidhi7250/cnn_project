import streamlit as st
from utils import predict
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Vision Dashboard",
    page_icon="🧠",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(to right, #e8f5e9, #f1f8e9);
}

/* Title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1b5e20;
}

.sub-title {
    text-align: center;
    color: #388e3c;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

/* Prediction Box */
.prediction-box {
    background: #dcedc8;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: #2e7d32;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🧠 AI Dashboard")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Dashboard", "📊 Model Info"]
)

# ---------------- HEADER ----------------
st.markdown(
    "<div class='main-title'>CNN Image Classification Dashboard</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Upload an image and let AI predict the class</div>",
    unsafe_allow_html=True
)

# ---------------- DASHBOARD PAGE ----------------
if page == "🏠 Dashboard":

    col1, col2 = st.columns([1, 1])

    # LEFT SIDE
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("📤 Upload Image")

        uploaded_file = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is not None:
            image = Image.open(uploaded_file)

            st.image(
                image,
                caption="Uploaded Image",
                use_container_width=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # RIGHT SIDE
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("🧠 Prediction Result")

        if uploaded_file is not None:

            if st.button("🚀 Predict Image"):

                image = Image.open(uploaded_file)

                prediction, confidence = predict(image)

                st.markdown(
                    f"""
                    <div class='prediction-box'>
                    Prediction: {prediction}<br><br>
                    Confidence: {confidence:.2f}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:
            st.info("Upload an image to start prediction.")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- MODEL INFO PAGE ----------------
elif page == "📊 Model Info":

    st.subheader("📊 Model Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model Type", "CNN")

    with col2:
        st.metric("Framework", "TensorFlow")

    with col3:
        st.metric("Prediction", "Image Classification")

    st.markdown("---")

    st.write("""
This application uses a Convolutional Neural Network (CNN)
to classify uploaded images into trained categories.
""")

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>🚀 Built using CNN + Streamlit</div>",
    unsafe_allow_html=True
)