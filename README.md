# 🎓 College OAIP Final Project: Desktop GUI Application

Comprehensive desktop software engineered as the final semester application for the **"Fundamentals of Algorithmization and Programming"** course at MTKP. Developed with professional architecture and custom cross-environment runtime configuration.

## 🛠️ Tech Stack & Architecture
* **Language:** Python 3.10+
* **GUI Framework:** PyQt5 (Dynamic UI parsing from components)
* **Database Relational Engine:** SQLite
* **Data Export Integration:** Automated compilation into HTML and Microsoft Word (.docx) formats

## 📁 Repository Structure & Modules
* `main.py` / `new_main.py` — Core application dispatcher and runtime loop initialization.
* `avt.py` / `regi.py` — Advanced user authentication and security encryption protocols.
* `table.py` — Dynamic data parsing grid with sorting and conditional formatting.
* `helpsql` — Dedicated SQL database tables cache.
* `glav.ui` / `avt.ui` — XML-based user interface templates designed via Qt Designer.

## ⚙️ Environment Configuration & Deployment Execution
The application features a built-in cross-platform runtime adapter depending on the host deployment environment:

1. **Production Environment (Mobile/Standard GUI UI):**
   Executes through the standard **`main_home`** pipeline for rendering native PyQt5 windows and handling standard user inputs.
2. **Development & Emulation Environment (Laptop Testing Architecture):**
   Executes through the dedicated **`emulator_db`** architecture to bypass hardware interface limits, enabling smooth database testing, validation, and debugging on portable hardware.

## 🚀 Key Features
1. **Multi-Module GUI Architecture:** Decoupled user interface layouts and backend controllers using clean OOP classes.
2. **Relational Database Storage:** Secure, structured CRUD operations bound to local SQLite database files.
3. **Automated Document Compilation:** Fast compilation of dynamic runtime tables directly into printable office formats.
