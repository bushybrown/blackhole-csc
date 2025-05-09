# === Enhanced Entropy Inspector with FFT Noise Signature and Full Integration ===

import json
import base64
import hashlib
import sys
import os
import statistics
from collections import Counter
from math import log2
from tkinter import filedialog, Tk, simpledialog, messagebox
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from colorama import Fore, Style, init
import matplotlib.pyplot as plt
import numpy as np
init(autoreset=True)

class NullSignatureCollapse:
    def __init__(self, output_dir="phantom_output"):
        self.output_dir = output_dir

    def reconstruct(self, null_map_path=None):
        if null_map_path is None:
            null_map_path = os.path.join(self.output_dir, "null_map.json")
        with open(null_map_path, "r") as f:
            null_map = json.load(f)
        ordered = sorted(null_map.items(), key=lambda x: x[1])
        data = b''.join(
            open(os.path.join(self.output_dir, fname), "rb").read()[16:]
            for fname, _ in ordered
        )
        return data

def decrypt_bhex_file(filepath, password):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        iv = base64.b64decode(data.get('iv', ''))
        cipher_data = base64.b64decode(data.get('cipher', ''))
        key = hashlib.sha256(password.encode()).digest()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(cipher_data), AES.block_size)
        return json.loads(decrypted)
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Failed to decrypt or parse .bhex file: {e}{Style.RESET_ALL}")
        return None

def decrypt_null_signature_bhex(password, map_path="phantom_output/null_map.json"):
    try:
        nullifier = NullSignatureCollapse()
        package_bytes = nullifier.reconstruct(map_path)
        key = hashlib.sha256(password.encode()).digest()
        iv = base64.b64decode(json.loads(package_bytes.decode())["iv"])
        cipher_data = base64.b64decode(json.loads(package_bytes.decode())["cipher"])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(cipher_data), AES.block_size)
        return json.loads(decrypted)
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Failed to decrypt or parse Null Signature package: {e}{Style.RESET_ALL}")
        return None

def shannon_entropy(data):
    if not data:
        return 0.0
    freq = Counter(data)
    total = len(data)
    return round(-sum((count / total) * log2(count / total) for count in freq.values()), 4)

def estimate_password_strength(password):
    variety = sum([any(c.islower() for c in password), any(c.isupper() for c in password),
                   any(c.isdigit() for c in password), any(not c.isalnum() for c in password)])
    if variety == 0:
        return 0
    estimated_bits = int(log2(pow(variety * 26, len(password))))
    return estimated_bits

def calculate_symbolic_strength(tags, drift_score, uniqueness_ratio):
    return min(600, 500 + len(tags)*2 + int(drift_score // 3) + int(uniqueness_ratio * 5))

def drift_volatility_index(shift_log):
    if len(shift_log) < 2:
        return 0.0
    return round(statistics.stdev(shift_log), 4)

def fusion_entropy_weight(fusion_map):
    return round(sum(v**2 for v in fusion_map.values()), 4) if fusion_map else 0.0

def symbol_skew(data):
    freq = Counter(data)
    if not freq:
        return 0.0
    most_common = freq.most_common(1)[0][1]
    least_common = freq.most_common()[-1][1]
    return round(most_common / (least_common + 1), 2)

def classify_behavior(volatility, saturation, skew):
    if volatility > 1e+12 and saturation > 0.4 and skew > 20:
        return "[🧠] Oracle Warp Pattern Detected"
    elif volatility < 100 and saturation < 0.1 and skew < 5:
        return "[🧊] Dormant Cipher Detected"
    elif volatility > 1000 and skew > 15:
        return "[⚠] Chaotic Core Behavior"
    else:
        return "[•] Structural Pattern Normalized"

def confidence_estimator(phantom_tags, volatility, skew):
    base = 60 + len(phantom_tags) * 2
    if volatility > 1000:
        base += 10
    if skew > 10:
        base += 10
    return min(base, 99)

def approximate_nist_tests(ciphertext):
    if not ciphertext:
        return {}
    bits = ''.join(f"{ord(c):08b}" for c in ciphertext if ord(c) < 128)
    ones = bits.count('1')
    zeros = bits.count('0')
    runs = sum(bits[i] != bits[i+1] for i in range(len(bits)-1))
    return {
        "bit_ones": ones,
        "bit_zeros": zeros,
        "bit_ratio": round(ones / max(1, len(bits)), 4),
        "bit_runs": runs,
        "bit_length": len(bits)
    }

def plot_entropy_graph(shift_log):
    if not shift_log:
        return
    plt.figure(figsize=(10, 4))
    plt.plot(shift_log, color='darkcyan', linewidth=1.5)
    plt.title("BlackHole Shift Log Drift")
    plt.xlabel("Index")
    plt.ylabel("Shift Value")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig("drift_plot.png")
    plt.close()

def plot_symbol_histogram(ciphertext):
    if not ciphertext:
        return
    freq = Counter(ciphertext)
    labels, values = zip(*freq.most_common())
    plt.figure(figsize=(10, 4))
    plt.bar(labels, values, color='orchid')
    plt.title("Symbol Frequency Histogram")
    plt.xlabel("Symbol")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("symbol_histogram.png")
    plt.close()

def plot_fft_of_shift_log(shift_log):
    if not shift_log:
        return
    y = np.array(shift_log)
    y_fft = np.abs(np.fft.fft(y))
    x = np.fft.fftfreq(len(y))

    anomalies = np.sum(y_fft[:len(y)//2] > 100)

    plt.figure(figsize=(10, 4))
    plt.plot(x[:len(x)//2], y_fft[:len(y_fft)//2], color='slateblue')
    plt.title(f"FFT Frequency Spectrum of Shift Log | Anomaly Peaks: {anomalies}")
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig("fft_shift_spectrum.png")
    plt.close()

def analyze_entropy_metrics(package, output_to_file=False):
    output_lines = []
    metrics = {}
    raw = package.get("cipher", "")
    metrics['symbol_count'] = len(raw)
    metrics['word_count'] = len(raw.split())
    metrics['symbol_density'] = round(metrics['symbol_count'] / (metrics['word_count'] + 1), 2)
    metrics['shannon_entropy'] = shannon_entropy(raw)
    metrics['symbol_skew'] = symbol_skew(raw)

    shift_log = package.get("shift_log", [])
    entropy_score = sum(shift_log)
    drift_range = max(shift_log) - min(shift_log) if shift_log else 1
    drift_score = round((entropy_score / (drift_range + 1)) % 100, 2)
    drift_volatility = drift_volatility_index(shift_log)

    tags = package.get("subconscious", [])
    phantom_tags = [t for t in tags if "PHANTOM" in t or "Δ" in t or "⌜" in t]
    tag_saturation = round(len(tags) / (metrics['word_count'] + 1), 2)

    fusion_map = package.get("fusion_map", {})
    fusion_summary = ", ".join(f"{k}:{v}" for k, v in fusion_map.items()) if fusion_map else "None"
    fusion_weight = fusion_entropy_weight(fusion_map)
    unique_symbols = len(set(raw.split()))
    uniqueness_ratio = round(unique_symbols / (metrics['word_count'] + 1), 3)
    password_strength = estimate_password_strength(package.get("password", ""))
    complexity_bits = calculate_symbolic_strength(tags, drift_score, uniqueness_ratio)
    behavior_class = classify_behavior(drift_volatility, tag_saturation, metrics['symbol_skew'])
    confidence = confidence_estimator(phantom_tags, drift_volatility, metrics['symbol_skew'])
    nist = approximate_nist_tests(raw)

    drift_bar = ''.join(['|' if s > 40 else ':' if s > 20 else '.' for s in shift_log[:60]])
    est_layers = 3 + (1 if fusion_map else 0) + (1 if phantom_tags else 0)

    anomalies = int(np.sum(np.abs(np.fft.fft(np.array(shift_log)))[:len(shift_log)//2] > 100))
    fft_classification = (
        "[•] Flat Spectrum (Stochastic)" if anomalies == 0 else
        "[⟳] Periodic Structure Detected" if anomalies <= 5 else
        "[⚠] Resonant Drift Activity" if anomalies <= 15 else
        "[🔊] High Entropy Pulse"
    )
    output_lines.append(f"FFT Anomaly Spikes Detected: {anomalies}")
    output_lines.append(f"FFT Classification: {fft_classification}")
    output_lines.extend([
        "\n=== 🔍 BLACKHOLE ENTROPY INSPECTION ===",
        f"Word Count:             {metrics['word_count']}",
        f"Symbol Count:           {metrics['symbol_count']}",
        f"Symbol Density:         {metrics['symbol_density']}",
        f"Shannon Entropy:        {metrics['shannon_entropy']}",
        f"Drift Score:            {drift_score}",
        f"Drift Volatility:       {drift_volatility}",
        f"Subconscious Tags:      {len(tags)} total | {len(phantom_tags)} phantom",
        f"Tag Saturation:         {tag_saturation}",
        f"Visual Drift Signature: {drift_bar}",
        f"Detected Layers:        {est_layers} (base + fusion/oracle flags)",
        f"Fusion Map:             {fusion_summary}",
        f"Fusion Entropy Weight:  {fusion_weight}",
        f"Symbol Uniqueness:      {unique_symbols} unique | Ratio: {uniqueness_ratio}",
        f"Symbol Frequency Skew:  {metrics['symbol_skew']}",
        f"Password Influence:     ~{password_strength} bits (est.)",
        f"NIST Approx Bit Ratio:  {nist['bit_ratio']} | Runs: {nist['bit_runs']}",
        "---------------------------------------",
        f"Symbolic Strength Index: 2^{complexity_bits} (~{round(complexity_bits / 3.32, 2)} decimal digits)",
        f"{behavior_class}",
        f"Confidence Level:       {confidence}%",
        "=======================================\n"
    ])

    print('\n'.join([Fore.CYAN + line + Style.RESET_ALL for line in output_lines]))
    if output_to_file:
        with open("entropy_report.txt", "w", encoding="utf-8") as f:
            f.write('\n'.join(output_lines))
        plot_entropy_graph(shift_log)
        plot_symbol_histogram(raw)
        plot_fft_of_shift_log(shift_log)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    use_null = messagebox.askyesno("B4.3?", "Analyze a B4.3 Null Signature Package?")
    password = simpledialog.askstring("Password", "Enter password:", show='*')
    if use_null:
        map_path = filedialog.askopenfilename(title="Select null_map.json", filetypes=[("JSON", "*.json")])
        pkg = decrypt_null_signature_bhex(password, map_path)
    else:
        filepath = filedialog.askopenfilename(title="Select .bhex File", filetypes=[("BlackHole Packages", "*.bhex")])
        pkg = decrypt_bhex_file(filepath, password)
    if pkg:
        pkg["password"] = password
        analyze_entropy_metrics(pkg, output_to_file=True)
        messagebox.showinfo("Analysis Complete", "All entropy visuals and FFT output saved.")
