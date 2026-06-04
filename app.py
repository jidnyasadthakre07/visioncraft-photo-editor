import streamlit as st
from PIL import Image
import cv2
import numpy as np
import io

st.set_page_config(page_title="Photo Editor", layout="wide")

st.title("📸 VisionCraft")
st.subheader("Intelligent Photo Editing Studio")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Read Image
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    st.sidebar.header("Image Controls")

    # -----------------------------
    # Resize
    # -----------------------------
    height, width = img.shape[:2]

    st.sidebar.subheader("Resize")

    new_width = st.sidebar.slider(
        "Width",
        100,
        2000,
        width
    )

    new_height = st.sidebar.slider(
        "Height",
        100,
        2000,
        height
    )

    img = cv2.resize(img, (new_width, new_height))

    # -----------------------------
    # Brightness & Contrast
    # -----------------------------
    st.sidebar.subheader("Adjustments")

    brightness = st.sidebar.slider(
        "Brightness",
        -100,
        100,
        0
    )

    contrast = st.sidebar.slider(
        "Contrast",
        0.5,
        3.0,
        1.0
    )

    img = cv2.convertScaleAbs(
        img,
        alpha=contrast,
        beta=brightness
    )

    # -----------------------------
    # Rotation
    # -----------------------------
    st.sidebar.subheader("Rotation")

    angle = st.sidebar.slider(
        "Rotate Image",
        0,
        360,
        0
    )

    if angle != 0:

        h, w = img.shape[:2]

        matrix = cv2.getRotationMatrix2D(
            (w // 2, h // 2),
            angle,
            1
        )

        img = cv2.warpAffine(
            img,
            matrix,
            (w, h)
        )

    # -----------------------------
    # Blur
    # -----------------------------
    st.sidebar.subheader("Blur")

    blur_value = st.sidebar.slider(
        "Blur Amount",
        1,
        25,
        1,
        step=2
    )

    if blur_value > 1:
        img = cv2.GaussianBlur(
            img,
            (blur_value, blur_value),
            0
        )

    # -----------------------------
    # Grayscale
    # -----------------------------
    if st.sidebar.checkbox("Grayscale"):

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_RGB2GRAY
        )

        img = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2RGB
        )

    # -----------------------------
    # Warm Filter
    # -----------------------------
    if st.sidebar.checkbox("Warm Filter"):

        warm_img = img.copy()

        warm_img[:, :, 0] = np.clip(
            warm_img[:, :, 0] * 1.1,
            0,
            255
        )

        warm_img[:, :, 2] = np.clip(
            warm_img[:, :, 2] * 0.9,
            0,
            255
        )

        img = warm_img.astype(np.uint8)

    # -----------------------------
    # Sharpen
    # -----------------------------
    if st.sidebar.checkbox("Sharpen"):

        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])

        img = cv2.filter2D(
            img,
            -1,
            kernel
        )

    # -----------------------------
    # Portrait Blur
    # -----------------------------
    if st.sidebar.checkbox("Portrait Blur"):

        blurred = cv2.GaussianBlur(
            img,
            (31, 31),
            0
        )

        h, w = img.shape[:2]

        mask = np.zeros(
            (h, w),
            dtype=np.uint8
        )

        cv2.circle(
            mask,
            (w // 2, h // 2),
            min(h, w) // 3,
            255,
            -1
        )

        mask = cv2.GaussianBlur(
            mask,
            (51, 51),
            0
        )

        mask = mask / 255.0

        result = np.zeros_like(img)

        for i in range(3):
            result[:, :, i] = (
                img[:, :, i] * mask
                + blurred[:, :, i] * (1 - mask)
            )

        img = result.astype(np.uint8)

    # -----------------------------
    # Edge Detection
    # -----------------------------
    if st.sidebar.checkbox("Edge Detection"):

        edges = cv2.Canny(
            img,
            100,
            200
        )

        img = cv2.cvtColor(
            edges,
            cv2.COLOR_GRAY2RGB
        )

    # -----------------------------
    # Sketch Effect
    # -----------------------------
    if st.sidebar.checkbox("Sketch Effect"):

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_RGB2GRAY
        )

        inverted = 255 - gray

        blur = cv2.GaussianBlur(
            inverted,
            (21, 21),
            0
        )

        inverted_blur = 255 - blur

        sketch = cv2.divide(
            gray,
            inverted_blur,
            scale=256
        )

        img = cv2.cvtColor(
            sketch,
            cv2.COLOR_GRAY2RGB
        )

    # -----------------------------
    # Cartoon Effect
    # -----------------------------
    if st.sidebar.checkbox("Cartoon Effect"):

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_RGB2GRAY
        )

        gray = cv2.medianBlur(
            gray,
            5
        )

        edges = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,
            9,
            9
        )

        color = cv2.bilateralFilter(
            img,
            9,
            250,
            250
        )

        img = cv2.bitwise_and(
            color,
            color,
            mask=edges
        )

    # -----------------------------
    # Flip
    # -----------------------------
    if st.sidebar.checkbox("Flip Horizontal"):
        img = cv2.flip(img, 1)

    if st.sidebar.checkbox("Flip Vertical"):
        img = cv2.flip(img, 0)

    # -----------------------------
    # Black & White
    # -----------------------------
    if st.sidebar.checkbox("Black & White"):

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_RGB2GRAY
        )

        _, bw = cv2.threshold(
            gray,
            127,
            255,
            cv2.THRESH_BINARY
        )

        img = cv2.cvtColor(
            bw,
            cv2.COLOR_GRAY2RGB
        )

    # -----------------------------
    # Display Images
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Edited Image")
        st.image(img, use_container_width=True)

    # -----------------------------
    # Download
    # -----------------------------
    result = Image.fromarray(img)

    buffer = io.BytesIO()

    result.save(
        buffer,
        format="PNG"
    )

    st.download_button(
        label="📥 Download Edited Image",
        data=buffer.getvalue(),
        file_name="edited_image.png",
        mime="image/png"
    )

else:
    st.info("Upload an image to start editing.")