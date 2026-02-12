import tkinter as tk
from tkinter import filedialog, messagebox

class SRTPDecryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SRTP Decryption Tool")
        self.root.configure(bg='black')

        # Create and set dark theme colors
        self.frame = tk.Frame(self.root, bg='black')
        self.frame.pack(padx=10, pady=10)

        self.label_title = tk.Label(self.frame, text="SRTP Decryption Tool", bg='black', fg='white', font=('Arial', 16))
        self.label_title.pack(pady=10)

        self.master_key_label = tk.Label(self.frame, text='Master Key:', bg='black', fg='white')
        self.master_key_label.pack(pady=5)
        self.master_key_entry = tk.Entry(self.frame, width=40)
        self.master_key_entry.pack(pady=5)

        self.salt_label = tk.Label(self.frame, text='Salt:', bg='black', fg='white')
        self.salt_label.pack(pady=5)
        self.salt_entry = tk.Entry(self.frame, width=40)
        self.salt_entry.pack(pady=5)

        self.profile_label = tk.Label(self.frame, text='SRTP Profile:', bg='black', fg='white')
        self.profile_label.pack(pady=5)
        self.profile_entry = tk.Entry(self.frame, width=40)
        self.profile_entry.pack(pady=5)

        self.file_button = tk.Button(self.frame, text='Select Input File', command=self.select_file, bg='gray', fg='white')
        self.file_button.pack(pady=10)

        self.decrypt_button = tk.Button(self.frame, text='Decrypt', command=self.decrypt_srtp, bg='green', fg='white')
        self.decrypt_button.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()

    def decrypt_srtp(self):
        # Placeholder for decryption logic
        try:
            master_key = self.master_key_entry.get()
            salt = self.salt_entry.get()
            profile = self.profile_entry.get()

            if not master_key or not salt or not profile:
                messagebox.showerror("Input Error", "Please fill in all fields.")
                return
            
            # Insert decryption logic here
            messagebox.showinfo("Success", "VoIP call decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = SRTPDecryptionApp(root)
    root.mainloop()