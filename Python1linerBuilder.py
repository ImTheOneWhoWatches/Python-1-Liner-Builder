import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import os
import subprocess
import tempfile
import ast


class PythonOneLinerBuilder:
    def __init__(self):
        """Initialize the encryption key and Fernet cipher."""
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_script(self, script_content: str) -> bytes:
        """Encrypt the Python script to make it unreadable."""
        return self.cipher.encrypt(script_content.encode())

    def validate_script(self, script_content: str):
        """Validate Python script syntax."""
        try:
            ast.parse(script_content)
        except SyntaxError:
            raise ValueError("Invalid Python script syntax detected.")

    def generate_one_liner(self, script_content: str) -> str:
        """Generate a secure one-liner to execute the encrypted script."""
        encrypted_content = self.encrypt_script(script_content)
        encrypted_data = encrypted_content.decode()

        one_liner = f"""
import os, subprocess, tempfile
from cryptography.fernet import Fernet

key = os.getenv('SCRIPT_KEY').encode()
cipher = Fernet(key)
script = cipher.decrypt(b'{encrypted_data}').decode()

# Save the decrypted script to a temporary file and execute it securely
with tempfile.NamedTemporaryFile(suffix='.py', delete=False, mode='w') as temp_file:
    temp_file.write(script)
    temp_filename = temp_file.name

try:
    subprocess.run(['python', temp_filename], check=True)
finally:
    os.remove(temp_filename)
"""
        return one_liner

    def save_one_liner_to_file(self, one_liner: str, output_filename: str):
        """Save the generated one-liner to a file."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, output_filename)

        try:
            with open(output_path, 'w') as f:
                f.write(one_liner)
            print(f"✅ One-liner saved to {output_path}")
        except IOError as e:
            print(f"❌ Failed to save one-liner: {e}")

    def open_file_picker(self) -> str:
        """Open a file picker dialog to select a Python script."""
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        return file_path


if __name__ == "__main__":
    builder = PythonOneLinerBuilder()
    print("🔍 Please select a Python script to encrypt and convert into a one-liner.")

    # Open file picker
    script_filename = builder.open_file_picker()

    if script_filename:
        try:
            with open(script_filename, 'r') as f:
                script_content = f.read()

            # Validate script
            builder.validate_script(script_content)

            # Generate the one-liner
            one_liner = builder.generate_one_liner(script_content)

            # Save the one-liner to a new file
            builder.save_one_liner_to_file(one_liner, 'one_liner.py')

            print("🚀 Use the one-liner with the environment variable SCRIPT_KEY set to the encryption key.")

        except FileNotFoundError:
            print("❌ Selected file not found.")
        except ValueError as ve:
            print(f"❌ Validation Error: {ve}")
        except Exception as e:
            print(f"❌ An error occurred: {e}")
    else:
        print("⚠️ No file selected.")
