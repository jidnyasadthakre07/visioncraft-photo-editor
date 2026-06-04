# 📸 VisionCraft – Intelligent Photo Editing Studio

> An advanced image processing and photo editing application built using Python, OpenCV, and Streamlit. VisionCraft enables users to enhance, transform, and stylize images in real time through an intuitive and interactive web interface.

---

## 🚀 Project Overview

VisionCraft is a feature-rich photo editing application that combines the power of OpenCV with the simplicity of Streamlit. Users can upload images, perform real-time enhancements, apply artistic effects, and download the edited image instantly.

The project demonstrates practical applications of Computer Vision, Image Processing, and Python Web Development while providing a clean and user-friendly experience.

---

## ✨ Features

### 📂 Image Management
- Upload JPG, JPEG, and PNG images
- Real-time image preview
- Download edited images

### 📐 Image Transformations
- Resize Image
- Rotate Image (0°–360°)
- Flip Horizontally
- Flip Vertically

### 🎚️ Image Adjustments
- Brightness Adjustment
- Contrast Adjustment

### 🎨 Filters & Effects
- Grayscale Conversion
- Blur Effect
- Sharpen Effect
- Warm Filter
- Black & White Effect

### 🖌️ Artistic Effects
- Sketch Effect
- Cartoon Effect
- Edge Detection
- Portrait Background Blur

---

## 🖥️ Application Workflow

```text
Upload Image
      ↓
Resize & Transform
      ↓
Adjust Brightness & Contrast
      ↓
Apply Filters & Effects
      ↓
Preview Edited Image
      ↓
Download Final Image
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| Streamlit | Web Application Framework |
| OpenCV | Image Processing & Computer Vision |
| NumPy | Numerical Computation |
| Pillow (PIL) | Image Handling |
| Git & GitHub | Version Control |

---

## 📁 Project Structure

```text
VisionCraft/
│
├── app.py
├── requirements.txt
├── README.md
│
├── screenshots/
│
└── sample_images/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jidnyasadthakre07/visioncraft-photo-editor.git

cd visioncraft-photo-editor
```

### 2️⃣ Create a Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

### 5️⃣ Open in Browser

```text
http://localhost:8501
```

---

## 📦 Requirements

Create a file named `requirements.txt` and add:

```text
streamlit
opencv-python
numpy
Pillow
```

Or install directly:

```bash
pip install streamlit opencv-python numpy pillow
```

---

## 📸 Supported Image Operations

### Basic Editing
- Resize Images
- Brightness Control
- Contrast Control

### Enhancement Filters
- Grayscale Filter
- Blur Filter
- Sharpen Filter
- Warm Tone Filter

### Advanced Effects
- Portrait Background Blur
- Edge Detection
- Sketch Effect
- Cartoon Effect
- Black & White Conversion

### Image Manipulation
- Rotation
- Horizontal Flip
- Vertical Flip

---

## 🧠 Computer Vision Concepts Used

This project applies several image processing techniques including:

- Gaussian Blurring
- Convolution Filtering
- Image Thresholding
- Edge Detection (Canny Algorithm)
- Adaptive Thresholding
- Bilateral Filtering
- Color Space Transformations
- Image Rotation & Affine Transformations
- Brightness and Contrast Manipulation

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building interactive web applications using Streamlit
- Working with OpenCV for image processing
- Applying computer vision algorithms
- Handling image uploads and downloads
- Creating real-world Python projects
- Designing user-friendly interfaces
- Using Git and GitHub for project management

---

## 🚀 Future Improvements

Future enhancements planned for VisionCraft include:

- Face Detection Based Portrait Blur
- Background Removal
- AI-Based Image Enhancement
- Image Cropping Tool
- Watermark Support
- Text Overlay Features
- Batch Image Processing
- Image Compression
- Custom Filter Creation

---

## 📊 Project Highlights

✔ Real-Time Image Processing

✔ Interactive User Interface

✔ Multiple Editing Tools

✔ Artistic Image Effects

✔ Downloadable Output

✔ Beginner-Friendly Design

✔ Scalable Architecture

✔ Computer Vision Integration

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 👨‍💻 Author

**Jidnyasa Thakre**

GitHub: https://github.com/jidnyasadthakre07

LinkedIn: https://www.linkedin.com/in/jidnyasathakre/

---
