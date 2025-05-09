# --- BlackHole .bhex Inspector Suite ---
# Version: 4.2
# Adds FFT-style entropy summary and symbol analysis

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
import json
import statistics
import base64
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
import os
from collections import Counter

class BhexInspector:
    def __init__(self, root):
        self.root = root
        self.root.title("BlackHole .bhex Inspector")
        self.root.geometry("1000x700")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.tabs = {}
        for section in ["Metadata", "Key Profile", "Shift Log", "Oracle Log", "Integrity", "Cipher Tools", "Entropy Summary", "Decrypt"]:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=section)
            self.tabs[section] = ScrolledText(frame, wrap='word')
            self.tabs[section].pack(expand=True, fill='both')

        self.chart_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.chart_tab, text="Drift Graph")

        self.load_button = tk.Button(root, text="Open .bhex File", command=self.load_bhex)
        self.load_button.pack(pady=5)

        self.current_data = None

    def load_bhex(self):
        file_path = filedialog.askopenfilename(filetypes=[("BlackHole Encrypted Files", "*.bhex")])
        if not file_path:
            return
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            self.current_data = data

            self.display_metadata(data.get("metadata"))
            self.display_key_profile(data.get("key_profile"))
            self.display_shift_log(data.get("shift_log"))
            self.display_oracle_log(data.get("subconscious"), data.get("fusion_metadata"))
            self.display_integrity(data)
            self.display_cipher_stats(data.get("cipher"))
            self.display_entropy_summary(data.get("cipher"))
            self.display_decrypt_tab()
            self.plot_drift(data.get("shift_log"))

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

    def display_metadata(self, metadata):
        box = self.tabs["Metadata"]
        box.delete("1.0", tk.END)
        if not metadata:
            box.insert(tk.END, "[!] No metadata field found.")
            return
        for key, value in metadata.items():
            box.insert(tk.END, f"{key}: {value}\n")

    def display_key_profile(self, profile):
        box = self.tabs["Key Profile"]
        box.delete("1.0", tk.END)
        if not profile:
            box.insert(tk.END, "[!] No key profile available.")
            return
        for key, value in profile.items():
            box.insert(tk.END, f"{key}: {value}\n")

    def display_shift_log(self, shift_log):
        box = self.tabs["Shift Log"]
        box.delete("1.0", tk.END)
        if not shift_log:
            box.insert(tk.END, "[!] No shift log available.")
            return
        box.insert(tk.END, f"Length: {len(shift_log)}\n")
        try:
            avg = round(statistics.mean(shift_log), 2)
            stddev = round(statistics.stdev(shift_log), 2) if len(shift_log) > 1 else 0
            drift_range = max(shift_log) - min(shift_log)
            box.insert(tk.END, f"Average Drift: {avg}\nVolatility: {stddev}\nSpread: {drift_range}\n\n")
        except:
            pass
        box.insert(tk.END, f"Shift Values:\n{shift_log}")

    def display_oracle_log(self, subconscious, fusion):
        box = self.tabs["Oracle Log"]
        box.delete("1.0", tk.END)
        if subconscious:
            box.insert(tk.END, "Subconscious Log:\n")
            for line in subconscious:
                box.insert(tk.END, f"- {line}\n")
        else:
            box.insert(tk.END, "[!] No subconscious log found.\n")
        if fusion:
            box.insert(tk.END, "\nFusion Metadata:\n")
            for key, value in fusion.items():
                box.insert(tk.END, f"{key}: {value}\n")

    def display_integrity(self, data):
        box = self.tabs["Integrity"]
        box.delete("1.0", tk.END)
        iv_present = 'iv' in data
        hmac_present = 'hmac' in data
        cipher_len = len(data.get("cipher", ""))
        box.insert(tk.END, f"IV Present: {'Yes' if iv_present else 'No'}\n")
        box.insert(tk.END, f"HMAC Present: {'Yes' if hmac_present else 'No'}\n")
        box.insert(tk.END, f"Ciphertext Length: {cipher_len} characters\n")

    def display_cipher_stats(self, cipher):
        box = self.tabs["Cipher Tools"]
        box.delete("1.0", tk.END)
        if not cipher:
            box.insert(tk.END, "[!] No ciphertext present.")
            return
        try:
            raw = base64.b64decode(cipher)
            byte_freq = {b: raw.count(b) for b in set(raw)}
            unique_bytes = len(byte_freq)
            entropy_est = round(statistics.stdev(raw), 2) if len(raw) > 1 else 0
            box.insert(tk.END, f"Unique Bytes: {unique_bytes}\nEstimated Byte-Level StdDev: {entropy_est}\n\n")
            box.insert(tk.END, "Byte Frequency Snapshot (top 10):\n")
            top_bytes = sorted(byte_freq.items(), key=lambda x: x[1], reverse=True)[:10]
            for b, count in top_bytes:
                box.insert(tk.END, f"Byte {b}: {count}\n")
        except Exception as e:
            box.insert(tk.END, f"Error decoding cipher: {e}")

    def display_entropy_summary(self, cipher):
        box = self.tabs["Entropy Summary"]
        box.delete("1.0", tk.END)
        if not cipher:
            box.insert(tk.END, "[!] No ciphertext to analyze.")
            return
        try:
            text = base64.b64decode(cipher).decode('utf-8', errors='ignore')
            counter = Counter(text)
            total = sum(counter.values())
            entropy = -sum((freq / total) * (statistics.log(freq / total, 2)) for freq in counter.values())
            unique = len(counter)
            skew = round(max(counter.values()) / (total / unique), 2) if unique else 0
            box.insert(tk.END, f"Word Count: ~{len(text.split())}\n")
            box.insert(tk.END, f"Symbol Count: {total}\n")
            box.insert(tk.END, f"Unique Symbols: {unique}\n")
            box.insert(tk.END, f"Shannon Entropy: {round(entropy, 4)}\n")
            box.insert(tk.END, f"Symbol Frequency Skew: {skew}\n")
        except Exception as e:
            box.insert(tk.END, f"Error in entropy analysis: {e}")

    def display_decrypt_tab(self):
        box = self.tabs["Decrypt"]
        box.delete("1.0", tk.END)
        if not self.current_data:
            box.insert(tk.END, "[!] No .bhex file loaded.")
            return
        box.insert(tk.END, "Enter password below and click 'Attempt Decrypt'\n\n")

        entry = tk.Entry(self.tabs["Decrypt"], show="*")
        entry.pack()

        def attempt():
            try:
                key = hashlib.sha256(entry.get().encode()).digest()
                iv = base64.b64decode(self.current_data["iv"])
                ct = base64.b64decode(self.current_data["cipher"])
                cipher = AES.new(key, AES.MODE_CBC, iv)
                pt = unpad(cipher.decrypt(ct), AES.block_size)
                decrypted = json.loads(pt.decode('utf-8'))

                messagebox.showinfo("Decrypted", pt.decode('utf-8'))

                self.display_key_profile(decrypted.get("key_profile"))
                self.display_shift_log(decrypted.get("shift_log"))
                self.display_oracle_log(decrypted.get("subconscious"), decrypted.get("fusion_metadata"))
                self.plot_drift(decrypted.get("shift_log"))

            except Exception as e:
                messagebox.showerror("Decryption Failed", str(e))

        button = tk.Button(self.tabs["Decrypt"], text="Attempt Decrypt", command=attempt)
        button.pack(pady=5)

    def plot_drift(self, shift_log):
        for widget in self.chart_tab.winfo_children():
            widget.destroy()
        if not shift_log or len(shift_log) < 2:
            tk.Label(self.chart_tab, text="No valid shift log to graph.").pack()
            return
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.plot(shift_log, color='purple')
        ax.set_title("Fractal Drift Plot")
        ax.set_xlabel("Position")
        ax.set_ylabel("Shift Value")
        canvas = FigureCanvasTkAgg(fig, master=self.chart_tab)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = BhexInspector(root)
    root.mainloop()