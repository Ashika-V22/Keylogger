# 🖥️ Safe Keylogger Simulator (Streamlit)

**Live web : https://keylogger.streamlit.app/**

This is a **safe and ethical keylogger simulation** built using **Streamlit**.  
It does **NOT** capture system-wide keystrokes.  
It only logs text typed inside the Streamlit text-area, making it suitable for demos and cybersecurity learning.

## 🚀 Features
- Logs only what the user voluntarily types in the UI
- Stores logs safely in `safe_keylog.txt`
- Clean and simple interface
- 100% safe (no background or OS-level key capture)

## 📂 Project Structure
your_project/
│── app.py
│── safe_keylog.txt   (auto-created)
└── requirements.txt

## ▶️ Run the App
```bash
streamlit run app.py



