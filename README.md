# 🛡️ Python One-Liner Builder

## 📚 **Overview**
The **Python One-Liner Builder** is a secure script encryption and execution tool that converts any Python script into an encrypted one-liner. This one-liner can securely decrypt and execute the original script while maintaining confidentiality.

---

## 🚀 **Features**
- **🔑 Script Encryption:** Encrypt Python scripts securely using `cryptography.fernet`.
- **📝 One-Liner Generation:** Generate a single Python command that decrypts and runs the script.
- **📂 File Picker GUI:** Easy-to-use file picker to select scripts.
- **🛡️ Secure Execution:** Decrypted scripts run in a temporary file.
- **🗑️ Cleanup:** Temporary files are automatically removed after execution.
- **✅ Syntax Validation:** Validates Python syntax before encryption.

---

## 💻 **Prerequisites**
Make sure you have the following dependencies installed:
- Python 3.11+
- `cryptography`
- `tkinter`

Install dependencies using pip:
```bash
pip install cryptography tk
```

---

## 🛠️ **How to Use**

### 1️⃣ **Run the Builder Script**
Run the main script to start the encryption process:
```bash
python main.py
```

### 2️⃣ **Select a Python Script**
- A file picker will appear.
- Select the Python script (`.py`) you want to encrypt.

### 3️⃣ **Generate One-Liner**
- The script generates an encrypted one-liner and saves it as `python main.py` in the current directory.

### 4️⃣ **Run the One-Liner**
Set the encryption key in your environment variable and execute:
```bash
export SCRIPT_KEY='your-key-here'
python main.py
```

---

## 🛡️ **Security Best Practices**
- Keep the encryption key (`SCRIPT_KEY`) secret.
- Avoid hardcoding sensitive information.
- Validate scripts before encrypting.
- Always set environment variables securely.

---

## 🐞 **Troubleshooting**
| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'cryptography'` | Install dependencies: `pip install cryptography` |
| `SCRIPT_KEY not set` | Export the key using: `export SCRIPT_KEY='your-key'` |
| Temporary file not deleted | Ensure cleanup logic is executed (handled in the script). |

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to fork the repository, submit issues, or open pull requests.

---

## 📜 **License**
This project is licensed under the MIT License.

---

✅ **Enjoy Secure Python Script Encryption!** 🐍✨
