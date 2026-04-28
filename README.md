# 📈 FitSync | Holistic Health Intelligence



**FitSync** is a Python-based health analytics platform that bridges the gap between physical biometrics and mental well-being. It combines data from **Apple Health** (physical) and **Daylio** (mental) to generate a unified **Recovery Score**.

---

## 🌐 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fitsync-project-archie-maini.streamlit.app/)

---

## 🚀 Key Features

* **Unified Dashboard:** View physical activity + mental state together
* **Trend Analysis:** Correlation heatmaps (sleep vs mood, steps vs mood)
* **Story Engine:** Simulated realistic correlations (demo mode)
* **Dynamic Uploads:** Upload Apple Health & Daylio CSV files
* **Modern UI:** Clean interface using Streamlit

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit
* **Data:** Pandas, Statsmodels
* **Visualization:** Plotly
* **Environment:** GitHub Codespaces

---

## 📁 Project Structure

```text
.
├── main.py              # Entry point (Streamlit app)
├── data/                # CSV storage
├── modules/             # Backend logic
│   ├── processor.py
│   ├── demo_story.py
│   └── interface.py
├── pages/               # Multi-page UI
│   ├── dashboard.py
│   ├── goals.py
│   └── trend.py
├── utils/               # Helper functions
├── requirements.txt
```

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/Saras-AI-Institute/Fitsync-project-Archie-Maini.git
cd Fitsync-project-Archie-Maini
pip install -r requirements.txt
streamlit run main.py
```

---

## 🧠 Core Idea

The **Recovery Score** combines:

* Heart Rate
* Sleep Duration
* Mood

👉 to tell how ready your body & mind are for the day.

---

## 🤖 AI Collaboration

This project was built using a **Human-in-the-loop AI workflow**:

* Architecture & logic → Designed manually
* AI tools (Gemini, Copilot) → Used for speed & debugging
* Data pipeline → Custom-built

---

## 👨‍💻 Author

**Archie Maini**
Software Development Student | Saras AI Institute
