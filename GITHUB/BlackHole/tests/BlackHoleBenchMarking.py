# === Cipher Benchmarking Lab with GUI ===

import os, json, base64, time, zlib, hashlib
import numpy as np
from Crypto.Cipher import AES, ChaCha20_Poly1305, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from collections import Counter
from math import log2
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk, Text, Button, Toplevel, Scrollbar, RIGHT, Y, LEFT, END, BOTH

# === Analysis Tools ===
def shannon_entropy(data):
    if not data:
        return 0.0
    freq = Counter(data)
    total = len(data)
    return round(-sum((count / total) * log2(count / total) for count in freq.values()), 4)

def nist_bits(text):
    bits = ''.join(f"{ord(c):08b}" for c in text if ord(c) < 128)
    ones = bits.count('1')
    runs = sum(bits[i] != bits[i+1] for i in range(len(bits)-1))
    return round(ones / max(1, len(bits)), 4), runs

def fft_spike_count(shift_vals):
    if not shift_vals:
        return 0
    y = np.array(shift_vals)
    y_fft = np.abs(np.fft.fft(y))
    return int(np.sum(y_fft[:len(y)//2] > 100))

def compressibility_ratio(data_bytes):
    if not data_bytes:
        return 1.0
    compressed = zlib.compress(data_bytes)
    return round(len(compressed) / len(data_bytes), 3)

# === Encryption Schemes ===
def encrypt_aes(text, key_size=128):
    key = get_random_bytes(key_size // 8)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(text.encode(), AES.block_size))
    return iv + ct

def encrypt_chacha(text):
    key = get_random_bytes(32)
    cipher = ChaCha20_Poly1305.new(key=key)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())
    return nonce + ciphertext + tag

def encrypt_rsa(text):
    key = RSA.generate(2048)
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(text.encode())

def load_blackhole_bhex():
    from tkinter.simpledialog import askstring
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select .bhex File", filetypes=[("BlackHole Package", "*.bhex")])
    if not file_path:
        return None
    password = askstring("Password", "Enter password for .bhex:", show='*')
    if not password:
        return None
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        iv = base64.b64decode(data["iv"])
        cipher_data = base64.b64decode(data["cipher"])
        key = hashlib.sha256(password.encode()).digest()
        aes = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(aes.decrypt(cipher_data), AES.block_size)
        package = json.loads(decrypted)
        return package.get("cipher", "")
    except Exception as e:
        print(f"Error loading .bhex: {e}")
        return None
    password = input("Enter password for .bhex: ")
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        iv = base64.b64decode(data["iv"])
        cipher_data = base64.b64decode(data["cipher"])
        key = hashlib.sha256(password.encode()).digest()
        aes = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(aes.decrypt(cipher_data), AES.block_size)
        package = json.loads(decrypted)
        return package.get("cipher", "")
    except Exception as e:
        print(f"Error loading .bhex: {e}")
        return None

def benchmark_cipher(label, func, text):
    start = time.time()
    try:
        result = func(text)
        runtime = round(time.time() - start, 4)
        if isinstance(result, bytes):
            encoded = result
        else:
            encoded = result.encode()

        entropy = shannon_entropy(encoded)
        result_str = result.decode('utf-8', errors='ignore') if isinstance(result, bytes) else result
        bit_ratio, bit_runs = nist_bits(result_str)
        comp_ratio = compressibility_ratio(encoded)
        spikes = fft_spike_count([ord(c) for c in result_str if c.isprintable()])

        return {
            "Cipher": label,
            "Entropy": entropy,
            "Bits(1%)": bit_ratio,
            "Runs": bit_runs,
            "FFT Spikes": spikes,
            "Compression": comp_ratio,
            "Time(s)": runtime
        }
    except Exception as e:
        return {"Cipher": label, "Error": str(e)}

def run_benchmark():
    message = "The quick brown fox jumps over the lazy dog 123!"
    results = []

    results.append(benchmark_cipher("AES-128", lambda t: encrypt_aes(t, 128), message))
    results.append(benchmark_cipher("AES-256", lambda t: encrypt_aes(t, 256), message))
    results.append(benchmark_cipher("ChaCha20", encrypt_chacha, message))
    results.append(benchmark_cipher("RSA-2048", encrypt_rsa, message))

    bh_cipher = load_blackhole_bhex()
    if bh_cipher:
        results.append(benchmark_cipher("BlackHoleV6 (.bhex)", lambda _: bh_cipher, message))

    output = "\n=== Cipher Benchmark Report ===\n"
    for r in results:
        if 'Error' in r:
            output += f"{r['Cipher']}: ERROR - {r['Error']}\n"
        else:
            output += f"{r['Cipher']:<22} Entropy: {r['Entropy']:<5} | Bits: {r['Bits(1%)']} | Runs: {r['Runs']:<4} | FFT: {r['FFT Spikes']:<3} | Comp: {r['Compression']} | Time: {r['Time(s)']}s\n"
    show_results(output)

def show_results(text):
    win = Toplevel()
    win.title("Benchmark Results")
    win.geometry("750x300")
    text_area = Text(win, wrap='word')
    scrollbar = Scrollbar(win, command=text_area.yview)
    text_area.configure(yscrollcommand=scrollbar.set)
    text_area.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_area.insert(END, text)
    text_area.config(state='disabled')

def launch_gui():
    root = Tk()
    root.title("BlackHole Cipher Benchmark")
    root.geometry("400x200")
    Button(root, text="Run Benchmark", font=("Arial", 14), command=run_benchmark).pack(pady=40)
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
