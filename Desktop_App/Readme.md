# 🖥️ Interest Calculator (Desktop Client)

## 📌 Overview
This is the **standalone desktop version** of the Interest Calculator. It allows users to calculate **Simple Interest (SI)** and **Compound Interest (CI)** easily.

## 🚀 Features
- Supports both **Simple Interest** & **Compound Interest** calculations
- User-friendly interface
- Lightweight & works **offline**
- Standalone **Windows executable (.exe)**

## 🛠️ Installation & Usage
### 🔹 **For Windows Users**
#### **Method 1: Run Pre-built EXE**
1. **Download** the latest `Interest_Calculator.exe` from the [Releases](https://github.com/GauravPowar/Interest_Calculator/releases).
2. Double-click to run the application.

#### **Method 2: Build from Source (For Developers)**
##### ✅ **Step 1: Install Python & Dependencies**
Ensure you have **Python 3.10+** installed. Then, install required dependencies:
```sh
pip install -r requirements.txt
```

##### ✅ **Step 2: Run the Python Script**
```sh
python interest_calculator.py
```

##### ✅ **Step 3: Convert to EXE (Windows Only)**
To create a standalone `.exe`, use **PyInstaller**:
```sh
pyinstaller --onefile --windowed interest_calculator.py
```
This will generate an `interest_calculator.exe` inside the `dist/` folder.

## 📝 Usage Instructions
1. Open the app.
2. Select **Simple Interest** or **Compound Interest**.
3. Enter **Principal Amount, Rate, and Time Period**.
4. Click **Calculate**.
5. View the results instantly!

## 🔧 Troubleshooting
- If Windows **blocks the EXE**, click **More Info → Run Anyway**.
- If `pyinstaller` is not recognized, ensure Python is added to your **system PATH**.
- For any issues, feel free to **create an Issue** on [GitHub](https://github.com/GauravPowar/Interest_Calculator/issues).

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Pull requests are welcome! If you’d like to improve the app, fork the repository and submit a PR.

## 🔗 Links
- **Web Version**: [Interest Calculator Web App](https://github.com/GauravPowar/Interest_Calculator/Web_App)
- **Report a Bug**: [Open an Issue](https://github.com/GauravPowar/Interest_Calculator/issues)

---
💡 _Developed by Gaurav Powar & @Up-And-Atom_ 🚀
