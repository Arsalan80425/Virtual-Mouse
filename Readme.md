# 🖱️ Virtual Mouse with Hand Tracking

Control your mouse cursor **just with your fingers** using your webcam!\
This project uses **OpenCV** and **MediaPipe** to detect your hand in real-time and move the mouse accordingly.

---

## 📌 Features

- ✅ Smooth mouse movement based on index finger position
- ✅ Single-click, continuous click, and right-click gestures
- ✅ Works with any standard webcam
- ✅ Lightweight — no deep learning model required

---

## 🎥 Demo

*(Add a GIF or screenshot here)*\
Example:

```bash
![Demo GIF](demo.gif)
```

---

## 📂 Project Structure

```
VirtualMouse/
│
├── final.py               # Main program
├── HandTrackingModule.py  # Hand detection helper
├── requirements.txt       # Python package dependencies
├── .gitignore              # Git ignore rules
└── README.md              # This file
```

---

## 🛠 Requirements

- Python **3.x** (check with `python --version`)
- Webcam

---

## 📦 Installation (Step-by-Step in VS Code)

1. **Clone this repository**

```bash
git clone https://github.com/Arsalan80425/Virtual-Mouse.git
cd Virtua-lMouse
```

2. **Create a virtual environment**

```bash
python -m venv myvenv
```

3. **Activate the virtual environment**

- **Windows PowerShell**

```powershell
.\myvenv\Scripts\Activate.ps1
```

- **Windows CMD**

```cmd
myvenv\Scripts\activate
```

- **Mac/Linux**

```bash
source myvenv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

1. Make sure your webcam is connected.
2. Run the script:

```bash
python final.py
```

3. Move your **index finger** to move the mouse.
4. Gestures:
   - ✌ **Index + middle fingers close together** → Single click
   - ☝ **Index + middle + ring fingers** → Continuous click
   - 👍 **Thumb + index only** → Right click

---

## ⚙️ How It Works

- **MediaPipe** detects hand landmarks.
- **OpenCV** processes webcam frames.
- Cursor position is mapped to your screen resolution using `numpy.interp`.
- **PyAutoGUI** moves the actual mouse.

---

## 📌 Notes

- Adjust `frameR` and `smoothening` in `final.py` for different responsiveness.
- Works best in **good lighting**.
- Disable mouse acceleration in OS for more precise control.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss your ideas.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

