# 🧾 Visitor Log System (Python Advanced)

A Python-based visitor logging system that records and manages visitor entries with timestamps, enforcing strict rules to prevent duplicate entries and control entry timing.

---

## 📌 Overview

This project simulates a real-world visitor management system using file handling and custom exception handling. It ensures that:

* A visitor cannot sign in more than once consecutively
* A minimum time gap (5 minutes) is enforced between entries
* All visitor activities are logged with timestamps

---

## 🚀 Features

* 📁 File handling using `with` statement
* ⏱️ Timestamp logging using `datetime`
* ❌ Custom exception handling:

  * `DuplicateVisitorError`
  * `TimeRestrictionError`
* 📄 Automatic file creation if files do not exist
* 🛡️ Graceful error handling (no program crash)
* 🧠 Real-world logic implementation

---

## 🛠️ Tech Stack

* Python
* `datetime` module
* File handling

---

## ⚙️ How It Works

1. User enters visitor name
2. System checks:

   * If visitor already signed in → raises `DuplicateVisitorError`
   * If last entry is within 5 minutes → raises `TimeRestrictionError`
3. If valid:

   * Entry is recorded with timestamp
   * Data is saved to file

---

## 🖥️ Sample Terminal Output

```bash
PS C:\Users\HomePC\Desktop\flash drive\python-advanced-visitor-log-system> & C:/Users/HomePC/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/HomePC/Desktop/flash drive/python-advanced-visitor-log-system/visitor_log.py"

Enter visitor's name: muhammad lawal mukhtar

Visitor added successfully
```

---

## 📂 Project Structure

```bash
python-advanced-visitor-log-system/
│
├── visitor_log.py
├── visitors.txt
├── output.txt
└── README.md
```

---

## ▶️ How to Run

```bash
# Navigate to project folder
cd python-advanced-visitor-log-system

# Run the program
python visitor_log.py
```

---

## 🎓 What You Will Learn

* File handling in Python (`with open`)
* Creating and using custom exceptions
* Working with timestamps using `datetime`
* Implementing real-world logic constraints
* Writing robust programs with error handling

---

## 🚧 Project Status

✅ Completed (Intermediate / Advanced Project)

---

## 🔮 Future Improvements

* Add graphical user interface (GUI)
* Store data in a database (SQLite/MySQL)
* Build an admin dashboard
* Support multiple visitor sessions
* Add login/authentication system

---

## 👨‍💻 Author

Imraan Mu'hd Sani

---
