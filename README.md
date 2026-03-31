
# 🚗 Automatic Number Plate Recognition System (ANPR)

A Computer Vision-based system that detects and recognizes vehicle number plates using OpenCV and EasyOCR, with a simple Streamlit dashboard for visualization.

---

## 📌 Features

* 📸 Real-time image capture using webcam
* 🔍 Number plate detection using contour-based approach
* 🧠 OCR-based text extraction (EasyOCR)
* 🧹 Automatic text cleaning using regex
* 💾 Data storage in CSV file (with timestamp)
* 🌐 Streamlit dashboard for visualization

---

## 🏗️ Project Structure

```
ANPR-System/
│
├── src/
│   ├── preprocessing.py
│   ├── edge_detection.py
│   ├── contour_detection.py
│   ├── masking.py
│   ├── ocr.py
│   ├── storage.py
│   ├── visualization.py
│   └── main.py
│
├── images/          # Captured images
├── output/          # Detected plates + CSV
├── app.py           # Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* **Python**
* **OpenCV**
* **EasyOCR**
* **NumPy**
* **Matplotlib**

---

## 🚀 How It Works

1. Capture image using webcam
2. Preprocess image (grayscale + filtering)
3. Detect edges using Canny
4. Find contours to locate number plate
5. Extract plate region
6. Apply OCR to read text
7. Clean and store results

---

## ▶️ Installation

```bash
git clone https://github.com/your-username/anpr-system.git
cd anpr-system

pip install -r requirements.txt
```

---

## 🖥️ Run the Project

### 🔹 Run Core ANPR System (Camera)

```bash
python src/main.py
```

Press:

* `c` → Capture image
* `q` → Quit

---


## 📊 Output

* Detected plate images saved in `/output`
* CSV file stores:

  * Plate Number
  * Timestamp

---

## 🧪 Example Output

* Input: Vehicle image
* Output: Extracted plate number (e.g., **KA51MG4525**)

---

## ⚠️ Limitations

* Sensitive to lighting conditions
* OCR accuracy depends on image quality
* May fail for highly tilted plates
* Contour detection not robust in complex backgrounds

---

## 🚀 Future Improvements

* Integrate YOLO for plate detection
* Improve OCR using deep learning models
* Add real-time video processing
* Cloud database integration
* Mobile app support

---

## 👨‍💻 Author

**Raju Kumar**
B.Tech CSE with AI & ML
Sandip University

---

## 📜 License

This project is for educational purposes.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
