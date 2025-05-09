# === B3.3 Proof Constrained Mapping Implementation ===
def logic_assert(condition, message, fallback_logic=None):
    """
    Triggers logic path redirect or mutation if a rule constraint fails.
    If fallback_logic is given, switch logic strategy mid-execution.
    """
    if not condition:
        log_debug(f"[B3.3 ERROR BENDING] Logic assertion failed: {message}")
        if (fallback_logic == "reverse_entropy"):
            log_debug("[B3.3] Switching to reverse entropy logic.")
            return "REVERSE"
        elif (fallback_logic == "phantom_layer"):
            log_debug("[B3.3] Injecting phantom logic layer.")
            return "PHANTOM"
        elif (fallback_logic == "skip_segment"):
            log_debug("[B3.3] Skipping corrupt message segment.")
            return "SKIP"
        else:
            log_debug("[B3.3] No fallback provided. Defaulting to soft exit.")
            return "FAIL"
    return "OK"

# === Example Usage in Encrypt Function ===
# Example of injecting logic assertion based on entropy and shift mismatch
    assertion_result = logic_assert(
        abs(len(encrypted) - len(shift_log)) < 3,
        "Shift log length deviates too far from message length.",
        fallback_logic="phantom_layer"
    )
    if (assertion_result == "PHANTOM"):
        # Insert a light phantom echo logic or skip real logic segment
        encrypted = encrypted[::-1]  # Simplified phantom effect for now
        log_debug("[B3.3] Phantom echo logic applied to encrypted message.")

# === B2.4 Boundary Blur Logic Implementation ===
# Retroactive Logic Fracture and Phantom Operator Injection

def inject_boundary_blur(message, shift_log, threshold=25000, fallback_branch="cubed_vowel"):
    """
    Checks for excessive entropy or shift values and retroactively mutates part of the message
    using a fallback branch logic like B1.1 (Cubed Vowel Logic).
    """
    blur_triggered = False
    max_shift = max(shift_log) if shift_log else 0

    if (max_shift >= threshold):
        blur_triggered = True
        midpoint = len(message) // 2
        prefix = message[:midpoint]
        suffix = message[midpoint:]

        # Apply Cubed Vowel Logic as fallback mutation
        vowel = find_first_vowel(prefix)
        y = get_cube_from_vowel(vowel) or 1
        cube_mod = 3  # default for fallback
        new_shifted = []

        for i, c in enumerate(prefix):
            cube_value = (y + i + 1) ** 3
            shift_val = apply_shift_formula(cube_value, cube_mod)
            new_shifted.append(shift_char(c, shift_val))

        message = ''.join(new_shifted) + suffix

    return message, blur_triggered


# === Usage Example in Encrypt Function ===
# Before final packaging
    encrypted, blur_triggered = inject_boundary_blur(encrypted, shift_log)
    if (blur_triggered):
        log_debug("[BLUR] Boundary Blur Logic activated: fallback logic applied to midpoint.")

# === Quantum Foam Drift Module for BlackHole OS V6 ===
FOAM_INTENSITY = 0.15
FOAM_STABILITY = 0.95

import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hmac


def pad(data):
    padding_len = 16 - (len(data) % 16)
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    padding_len = data[-1]
    #  Validate padding
    if (padding_len < 1 or padding_len > 16):
        raise ValueError("Invalid padding.")
    return data[:-padding_len]

def encrypt_aes(data_bytes, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data_bytes))
    return iv, encrypted

def decrypt_aes(encrypted_bytes, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted_bytes)
    return unpad(decrypted)

def generate_hmac(data_bytes, key):
    return hmac.new(key, data_bytes, hashlib.sha256).digest()

def verify_hmac(data_bytes, key, received_hmac):
    expected = generate_hmac(data_bytes, key)
    return hmac.compare_digest(expected, received_hmac)

# === Quantum Foam Logic ===

# === Quantum Foam Drift Module for BlackHole OS V6 ===
FOAM_INTENSITY = 0.15
FOAM_STABILITY = 0.95

def foam_drift(shift_val, foam_intensity=FOAM_INTENSITY):
    fluctuation = random.uniform(-foam_intensity * shift_val, foam_intensity * shift_val)
    return max(1, int(shift_val + fluctuation))

def foam_ghost_output(char, stability=FOAM_STABILITY):
    r = random.random()
    # 📐 For .bhex safety: always return char (no doubling or deletion)
    return char

def generate_planck_noise(seed, length=1024):
    digest = hashlib.sha256(seed.encode()).hexdigest()
    random.seed(int(digest, 16))
    return [random.randint(-2, 2) for _ in range(length)]

def apply_quantum_foam_shift(char, shift_val, foam_array, index):
    foam_shift = foam_drift(shift_val)
    noise = foam_array[index % len(foam_array)]
    total_shift = foam_shift + noise

    if (char.isalpha()):
        base = ord('A') if char.isupper() else ord('a')
        shifted_char = chr((ord(char) - base + total_shift) % 26 + base)
    else:
        shifted_char = char

    return foam_ghost_output(shifted_char)

# === CONTINUED ORIGINAL CODE ===

# (Reinserting full original BlackHole OS code here)

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import os
import pyperclip
import time
import itertools
import random
from threading import Thread
import hashlib
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from numba import njit
import json

# Patched full BlackHole OS with .bhex file dialog support

# === Fractal Memory Drift Injection (B3.2) and Decay ===
def decay_fractal_memory(memory: dict, mode: str = "linear", strength: float = 0.1) -> dict:
    """
    Apply decay or mutation to fractal memory.
    Modes:
      - 'linear'   : slowly reduce shift impact
      - 'wobble'   : small random drift up/down
      - 'mutate'   : overwrite values if entropy threshold breached
    """
    decayed_log = []
    for i, shift in enumerate(memory["shift_log"]):
        if (mode == "linear"):
            decayed = max(1, int(shift * (1 - strength)))
        elif (mode == "wobble"):
            drift = random.randint(-2, 2)
            decayed = max(1, shift + drift)
        elif (mode == "mutate"):
            if (memory["entropy_score"] > 1000 and i % 5 == 0):
                decayed = random.randint(5, 50)
            else:
                decayed = shift
        else:
            decayed = shift  # fallback
        decayed_log.append(decayed)

    memory["shift_log"] = decayed_log
    return memory


def log_fractal_memory(message: str, shift_log: list[int]) -> dict:
    """
    Store essential shift data and positional entropy from the first encryption pass.
    """
    entropy = sum(ord(c) for c in message)
    memory = {
        "message_length": len(message),
        "shift_log": shift_log,
        "entropy_score": entropy,
        "position_bias": [(i % 7) - (s % 3) for i, s in enumerate(shift_log)],
    }
    return memory

def apply_fractal_shift(message: str, memory: dict) -> str:
    """
    Use previously stored memory to mutate the message.
    """
    result = []
    for i, char in enumerate(message):
        shift = memory["shift_log"][i % len(memory["shift_log"])]
        bias = memory["position_bias"][i % len(memory["position_bias"])]
        new_char = chr(((ord(char) + shift + bias) % 126) or 32)
        result.append(new_char)
    return ''.join(result)


# === Hook Fractal Memory into Encryption Pass ===
# Modifying existing encrypt() function to inject recursive memory drift
# The following is placed after main encryption block and before final .bhex packaging

# Add to encrypt() after main encryption logic:
# memory = log_fractal_memory(encrypted, shift_log)
# encrypted = apply_fractal_shift(encrypted, memory)

# This creates a recursive drift encryption and makes each pass unique to its memory state

# Now integrated into canvas

# Patched full BlackHole OS with .bhex file dialog support

import ttkbootstrap as ttk
# ... (existing full system continues unchanged below)

# Inside your encrypt() function, insert:
# Hooking in fractal memory after core encryption logic

def encrypt(message, key):
    # ... existing fusion + encryption logic here ...
    encrypted, shift_log = encrypt_message(message, fibonacci_sequence, key, oracle_bias, rotor)

    # === Injecting Fractal Memory Drift (B3.2)
    memory = log_fractal_memory(encrypted, shift_log)
    encrypted = apply_fractal_shift(encrypted, memory)

    # === B3.3 Logic Assertion (Proof Constrained Mapping)
    assertion_result = logic_assert(
        abs(len(encrypted) - len(shift_log)) < 3,
        "Shift log length deviates too far from message length.",
        fallback_logic="phantom_layer"
    )
    if (assertion_result == "PHANTOM"):
        encrypted = encrypted[::-1]  # Simplified phantom fallback
        log_debug("[B3.3] Phantom echo logic applied to encrypted message.")

    # === Injecting Fractal Memory Drift ===
    memory = log_fractal_memory(encrypted, shift_log)
    encrypted = apply_fractal_shift(encrypted, memory)

    return encrypted

# Patched full BlackHole OS with .bhex file dialog support

# === Fractal Memory Drift Injection (B3.2) ===
def log_fractal_memory(message: str, shift_log: list[int]) -> dict:
    """
    Store essential shift data and positional entropy from the first encryption pass.
    """
    entropy = sum(ord(c) for c in message)
    memory = {
        "message_length": len(message),
        "shift_log": shift_log,
        "entropy_score": entropy,
        "position_bias": [(i % 7) - (s % 3) for i, s in enumerate(shift_log)],
    }
    return memory

def apply_fractal_shift(message: str, memory: dict) -> str:
    """
    Use previously stored memory to mutate the message.
    """
    result = []
    for i, char in enumerate(message):
        shift = memory["shift_log"][i % len(memory["shift_log"])]
        bias = memory["position_bias"][i % len(memory["position_bias"])]
        new_char = chr(((ord(char) + shift + bias) % 126) or 32)
        result.append(new_char)
    return ''.join(result)


# Patched full BlackHole OS with .bhex file dialog support

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import os
import pyperclip
import time
import itertools
import random
from threading import Thread
import hashlib
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from numba import njit
import json

DEBUG_MODE = True

current_package = {}  #  Ensure global variable is defined

# === Phantom Rotor Core ===
class RotorState:
    def __init__(self, runs=0):
        self.runs = runs
        self.rotor_a = self.get_rotor_a()
        self.rotor_b = self.get_rotor_b()
        self.rotor_c = self.get_rotor_c()

    def get_rotor_a(self):
        # Time-based drift rotor (hour of day)
        return sum(int(d) for d in time.strftime('%H')) % 10

    def get_rotor_b(self):
        # Message-count rotor
        return (self.runs % 7) + 1

    def get_rotor_c(self):
        # Oracle memory drift-based rotor
        try:
            with open("oracle_memory.json", "r") as f:
                mem = json.load(f)
                drift_sum = sum(run["drift_score"] for run in mem["runs"][-3:])
                return int(drift_sum) % 9
        except:
            return 3

    def rotate(self):
        self.runs += 1
        self.rotor_a = self.get_rotor_a()
        self.rotor_b = self.get_rotor_b()
        self.rotor_c = self.get_rotor_c()

    def total_bias(self):
        return self.rotor_a + self.rotor_b + self.rotor_c

# === B5.1 Fusion Engine ===
def charlie_protocol_trigger(fusion_history: list[dict], threshold: float = 0.85) -> bool:
    """
    Detects profile convergence over recent fusion decisions.
    If average similarity between recent fusion paths exceeds threshold,
    trigger logic mutation to prevent profiling.
    """
    def similarity(a, b):
        all_keys = set(a) | set(b)
        return sum(min(float(a.get(k, 0)), float(b.get(k, 0))) for k in all_keys) / max(sum(float(v) for v in a.values()), 1)

    filtered = [entry.get("fusion_map", {}) for entry in fusion_history if isinstance(entry.get("fusion_map", {}), dict)]
    if (len(filtered) < 3):
        return False

    recent = filtered[-3:]
    sims = [similarity(recent[i], recent[i + 1]) for i in range(2)]
    avg_sim = sum(sims) / len(sims)
    return avg_sim >= threshold


def adjust_branch_weights(prior_sessions: list[dict]) -> dict:
    """
    Create weight bias toward frequently-used branches.
    This is the 'white matter' influencing future cognition.
    """
    weight_bias = {}
    for session in prior_sessions[-3:]:  # Look at last 3 messages
        for branch, weight in session.get("fusion_weights", {}).items():
            weight_bias[branch] = weight_bias.get(branch, 0) + weight

    # Normalize weights
    total = sum(weight_bias.values())
    return {k: v / total for k, v in weight_bias.items()}


def analyze_entropy_profile(message, key, oracle_bias):
    entropy = sum(ord(c) for c in message)
    key_score = len(key) + sum(c.isdigit() for c in key) * 2 + sum(not c.isalnum() for c in key) * 3
    fusion_threshold = 2500
    entropy_modifier = entropy + key_score + oracle_bias.get("bias", 0) * 10
    activate_fusion = entropy_modifier > fusion_threshold
    fusion_map = {
        "B1.2": 0.55,
        "B3.1": 0.25,
        "B4.1": 0.20
    } if activate_fusion else {}
    return {
        "activate_fusion": activate_fusion,
        "fusion_map": fusion_map,
        "reason": f"Entropy+Key Score={entropy_modifier} ({'activated' if activate_fusion else 'not activated'})"
    }

def invoke_fusion_logic(message, key, fusion_map):
    log_debug(f"[FUSION] Activating Entropic Fusion Node with branches: {fusion_map}")
    fibonacci_sequence = generate_fibonacci_sequence(100000)
    return encrypt_message(message, fibonacci_sequence, key)  # Simplified shift log

def load_oracle_memory(path="oracle_memory.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"runs": []}

def calculate_drift_score(entropy, shift_log):
    try:
        spread = max(shift_log) - min(shift_log) if shift_log else 1
        #  Clamp to 100.0 max to avoid overflow
        return round(min((entropy / (spread + 1)) % 100, 100.0), 2)
    except OverflowError:
        return 99.99

def generate_oracle_bias(memory):
    recent = memory["runs"][-5:] if len(memory["runs"]) >= 5 else memory["runs"]
    if (not recent):
        return {"bias": 0, "state": "BALANCE", "response": "ΨEchoSelf>NEUTRAL>Σ1 :: Conditions stable."}

    avg_drift = sum(run["drift_score"] for run in recent) / len(recent)
    if (avg_drift > 75):
        return {"bias": -1, "state": "CHAOS_AVERSION", "response": "∴EchoSelf>STABILIZE>Δ1 :: Drift beyond tolerance."}
    elif (avg_drift < 30):
        return {"bias": 1, "state": "ENTROPY_HUNGER", "response": "∵EchoSelf>EXPAND>Ω3 :: Entropy suboptimal."}
    else:
        return {"bias": 0, "state": "BALANCE", "response": "ΨEchoSelf>NEUTRAL>Σ1 :: Conditions stable."}

def log_debug(message):
    if (DEBUG_MODE):
        print(f"[DEBUG] {time.ctime()} - {message}")

@njit
def _fast_fib(depth):
    sequence = np.empty(depth, dtype=np.int64)
    sequence[0] = 1
    sequence[1] = 1
    for i in range(2, depth):
        sequence[i] = sequence[i-1] + sequence[i-2]
    return sequence

_fib_cache = None
_fib_depth = 0

def generate_fibonacci_sequence(depth):
    global _fib_cache, _fib_depth
    if (_fib_cache is None or _fib_depth < depth):
        _fib_cache = _fast_fib(depth)
        _fib_depth = depth
    return _fib_cache

def key_to_modifiers(key):
    hashed = hashlib.sha256(key.encode()).hexdigest()
    nums = [int(char, 16)**2 for char in hashed[:16]]
    fib_mod = sum(nums[:5]) % 1000
    cube_mod = sum(nums[5:10]) % 7
    shift_mod = sum(nums[10:]) % 3
    return fib_mod, cube_mod, shift_mod

def get_cube_from_vowel(vowel):
    cube_map = {'A': 6, 'E': 7, 'I': 8, 'O': 9, 'U': 11}
    return cube_map.get(vowel.upper(), None)

def find_first_vowel(text):
    for char in text.upper():
        if (char in "AEIOU"):
            return char
    return None

def find_nth_vowel(text, n):
    count = 0
    for char in text.upper():
        if (char in "AEIOU"):
            count += 1
            if (count == n):
                return char
    return None

def shift_char(char, shift):
    if (char.isalpha()):
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    else:
        return char

def apply_shift_formula(cube_value, cube_mod):
    x = ((cube_value / 2) + 10) / 3 + cube_mod
    return int(x) + 1 if x % 1 != 0 else int(x)

def encrypt_message(message, fibonacci_sequence, key, oracle_bias=None, rotor=None):
    fib_mod, cube_mod, shift_mod = key_to_modifiers(key)
    if (oracle_bias and rotor):
        fib_mod += oracle_bias.get("bias", 0) + rotor.rotor_a
        cube_mod += oracle_bias.get("bias", 0) + rotor.rotor_b
        shift_mod += rotor.rotor_c
    # Oracle bias already applied above if conditions met
    words = message.split()
    encrypted = []
    shift_log = []
    y = get_cube_from_vowel(find_first_vowel(message)) or 1
    cube_index = 0
    fibonacci_mode = False

    for index, word in enumerate(words):
        if (index > 0):
            encrypted.append(' ')
            shift_log.append(0)

        if (not fibonacci_mode):
            if (len(word) >= 5):
                fibonacci_mode = True

            for char in word:
                cube_value = (y + cube_index + shift_mod) ** 3
                shift_val = apply_shift_formula(cube_value, cube_mod)
                shift_log.append(shift_val)
                encrypted.append(shift_char(char, shift_val))
                cube_index += 1
        else:
            third_vowel = find_nth_vowel(message, 3)
            special_end_letters = {'D', 'H', 'L', 'M', 'N', 'T'}
            first_long_word = next((w for w in words if len(w) >= 5), '')
            if (first_long_word and first_long_word[-1].upper() in special_end_letters):
                start_index = int(np.where(fibonacci_sequence == 701408733)[0][0])
            else:
                vowel_start_points = {'A': 4181, 'E': 28657, 'I': 10946, 'O': 13, 'U': 75025}
                start_point = vowel_start_points.get(third_vowel, 377)
                try:
                    start_index = int(np.where(fibonacci_sequence == (start_point + fib_mod))[0][0])
                except IndexError:
                    start_index = 377

            fib_shifts = fibonacci_sequence[start_index:]
            rest = ' '.join(words[index:])
            for i, char in enumerate(rest):
                shift_val = fib_shifts[i % len(fib_shifts)]
                shift_log.append(shift_val)
                encrypted.append(shift_char(char, shift_val))
            break

    return ''.join(encrypted), shift_log

def decrypt_message(encrypted_message, shift_values):
    decrypted = []
    for i, char in enumerate(encrypted_message):
        if (char.isalpha()):
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base - shift_values[i]) % 26 + base)
            decrypted.append(shifted)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# AxiomCore Symbol Layer
PUNCTUATION_CHARS = list(".,?!:;'\"-_()[]{}@#$%^&*+=<>/\\|~")
SYMBOL_WIDTH = 4
ALL_SYMBOLS = [''.join(p) for p in itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=SYMBOL_WIDTH)]
digit_symbols = {str(d): [s for s in ALL_SYMBOLS if str(d) not in s][:10] for d in range(10)}
punct_symbols = {p: [s for s in ALL_SYMBOLS if p not in s][:10] for p in PUNCTUATION_CHARS}

symbol_pool = {}
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    filtered = [s for s in ALL_SYMBOLS if letter not in s]
    symbol_pool[letter] = {
        'upper': filtered[:1000],
        'lower': filtered[1000:2000]
    }

symbol_map = {chr(i + 65): str(i + 1).zfill(2) for i in range(26)}
symbol_map.update({chr(i + 97): str(i + 27).zfill(2) for i in range(26)})
reverse_map = {v: k for k, v in symbol_map.items()}

def encrypt_1to1(message):
    session_pools = {letter: {
        'upper': random.sample(symbol_pool[letter]['upper'], len(symbol_pool[letter]['upper'])),
        'lower': random.sample(symbol_pool[letter]['lower'], len(symbol_pool[letter]['lower']))
    } for letter in symbol_pool}
    words = message.split()
    encrypted_words = []
    shared_log = []
    for word in words:
        encrypted = ''
        for c in word:
            # Uppercase letter
            if (c.isupper()):
                pool = session_pools.get(c.upper(), {}).get('upper', [])
                symbol = pool.pop() if pool else 'UNKN'
                shared_log.append((c, symbol))
            # Lowercase letter
            elif (c.islower()):
                pool = session_pools.get(c.upper(), {}).get('lower', [])
                symbol = pool.pop() if pool else 'unkn'
                shared_log.append((c, symbol))
            # Digit
            elif (c in digit_symbols):
                symbol = random.choice(digit_symbols[c])
                shared_log.append((c, symbol))
            # Punctuation
            elif (c in punct_symbols):
                symbol = random.choice(punct_symbols[c])
                shared_log.append((c, symbol))
            # Catch-all
            else:
                symbol = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=SYMBOL_WIDTH))
                shared_log.append((c, symbol))
            encrypted += symbol
        encrypted_words.append(encrypted)
    with open("shared_symbol_log.txt", "w") as f:
        for i, char in enumerate(shared_log):
            f.write(f"{i}:{char}\n")

    return ' '.join(encrypted_words), shared_log

def decrypt_1to1(cipher):
    try:
        shared_log = current_package.get("shared_symbols", [])
    except Exception as e:
        log_debug(f"[DECRYPT] Failed to load shared symbol log from current_package: {e}")
        shared_log = []

    words = cipher.strip().split()
    decrypted_words = []
    counter = 0
    for word in words:
        # Pad word if length isn't divisible by 4 to prevent symbol shift
        while (len(word) % SYMBOL_WIDTH != 0):
            word += '_'
        symbols = [word[i:i+SYMBOL_WIDTH] for i in range(0, len(word), SYMBOL_WIDTH)]
        decrypted = ''
        for symbol in symbols:
            # Treat _ as transparent for symbol matching
            if (symbol.endswith('_')):
                symbol = symbol.rstrip('_')
            if (counter < len(shared_log)):
                expected = shared_log[counter]
                if (expected[1] is None):
                    decrypted += expected[0] if expected[0] is not None else symbol
                elif (symbol == expected[1]):  # Exact match
                    decrypted += expected[0]
                else:
                    guessed = reverse_map.get(symbol)
                    if (not guessed):
                        # Strip padding chars or attempt Hamming fallback if needed
                        guessed = '?'
                    decrypted += guessed
                counter += 1
            else:
                decrypted += '?'
        decrypted_words.append(decrypted)
    return ' '.join(decrypted_words)

def generate_subconscious_log(message, key, shift_log):
    try:
        entropy = sum(ord(c) for c in message) + min(np.clip(sum(shift_log), 0, 1_000_000), 1_000_000)
        if (entropy <= 0):
            entropy = 1
        digest = hashlib.sha256(f"{key}{entropy}".encode()).hexdigest()
        seed = int(digest, 16) % 10_000_000
        random.seed(seed)
        symbols = ['⟁', '⌬', '∴', 'Δ', '⇄', 'Ω', 'π', 'Σ', '⊗', '≡', '∵', 'Ψ']
        tags = ['B1.1', 'B1.2', 'SHIFT', 'PATH_MUT', 'CHAOS', 'ECHO', 'RECALL', 'GLYPH']
        fragments = []
        for _ in range(random.randint(8, 16)):
            symbol = random.choice(symbols)
            tag = random.choice(tags)
            num = random.randint(10, 999)
            fragments.append(f"{symbol}{tag}>{num}")
        if (random.random() > 0.5):
            fragments.insert(random.randint(1, len(fragments)-1), f"∵PHANTOM>Δ{random.randint(1,9)}")
        return fragments
    except Exception as e:
        log_debug(f"[SUBCONSCIOUS ERROR] {e}")
        return ["∵FAILSAFE>Δ0"]

# === Parasite Memory System ===
def load_parasite_memory(path="parasite_memory.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "drift_bias": 0,
            "influence_count": 0,
            "history": [],
            "fractal_history": []
        }

def update_parasite_memory(drift_score, entropy_value):
    memory = load_parasite_memory()
    parasite_bias = int((drift_score + (entropy_value % 97)) % 7)
    memory["drift_bias"] += parasite_bias
    memory["influence_count"] += 1
    memory["history"].append({
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
        "bias_added": parasite_bias,
        "entropy": entropy_value,
        "drift": drift_score
    })
    if (len(memory["history"]) > 20):
        memory["history"] = memory["history"][-20:]
    with open("parasite_memory.json", "w") as f:
        json.dump(memory, f, indent=4)
    return memory

def generate_random_fusion():
    #  Placeholder for CHARLIE protocol
    return {
        "B1.1": round(random.uniform(0.3, 0.6), 2),
        "B3.1": round(random.uniform(0.2, 0.4), 2),
        "B4.1": round(random.uniform(0.1, 0.3), 2),
    }

def encrypt():
    global current_package
    oracle_memory = load_oracle_memory()
    oracle_bias = generate_oracle_bias(oracle_memory)

    # === ROTOR MAGIC ===
    rotor = RotorState(runs=len(oracle_memory["runs"]))
    rotor.rotate()
    log_debug(f"[ROTORS] A: {rotor.rotor_a}, B: {rotor.rotor_b}, C: {rotor.rotor_c}")
    log_debug(f"[ORACLE STATE] {oracle_bias['state']}: {oracle_bias['response']}")
    global current_package

    def analyze_key(key):
        profile = {
            'vowel_count': sum(1 for c in key if c.lower() in 'aeiou'),
            'digit_count': sum(1 for c in key if c.isdigit()),
            'symbol_count': sum(1 for c in key if not c.isalnum()),
            'length': len(key)
        }
        profile['branch_path'] = []
        if (profile['vowel_count'] > 4):
            profile['branch_path'].append("B1.1")
        if (profile['digit_count'] > 3):
            profile['branch_path'].append("B1.2")
        if (profile['symbol_count'] >= 1):
            profile['branch_path'].append("B2.1")
        return profile

    root.config(cursor="watch")
    root.update()

    message = input_text.get("1.0", tk.END).strip()
    #  Null/empty check
    if (not message.strip()):
        messagebox.showwarning("⚠️ Warning", "Please enter a message to encrypt.")
        return

    message = convert_numbers_to_words(message)
    if (not message):
        messagebox.showwarning("⚠️ Warning", "Please enter a message to encrypt.")
        return

    key = simpledialog.askstring("🔑 Encryption Key", "Enter encryption key:", show='*', parent=root)
    confirm_key = simpledialog.askstring("🔑 Confirm Key", "Re-enter the encryption key:", show='*', parent=root)
    if (key != confirm_key):
        messagebox.showerror("❌ Error", "Keys do not match. Encryption cancelled.")
        return
    if (rotor.runs % 5 == 0):
        key += f"∴{rotor.total_bias()}Ψ"
    if (not key):
        messagebox.showwarning("⚠️ Warning", "Encryption key is required.")
        return

    fib_mod, cube_mod, shift_mod = key_to_modifiers(key)
    fibonacci_sequence = generate_fibonacci_sequence(100000)
    fib_mod += oracle_bias["bias"]
    cube_mod += oracle_bias["bias"]
    fusion_decision = analyze_entropy_profile(message, key, oracle_bias)
    log_debug(f"[FUSION DECISION] {fusion_decision['reason']}")

    # === CHARLIE PROTOCOL ===
    if (charlie_protocol_trigger(oracle_memory['runs'])):
        fusion_decision['fusion_map'] = generate_random_fusion()
        log_debug("[CHARLIE PROTOCOL] Triggered. Fusion map scrambled to avoid profile convergence.")

    if (fusion_decision["activate_fusion"]):
                encrypted, shift_log = invoke_fusion_logic(message, key, fusion_decision["fusion_map"])
    else:
                encrypted, shift_log = encrypt_message(message, fibonacci_sequence, key, oracle_bias, rotor)

    log_debug(f"[ENCRYPT] BlackHole result: {encrypted}")
    log_debug(f"[ENCRYPT] BlackHole char count: {len(encrypted)}")
    log_debug(f"[ENCRYPT] Shift log length: {len(shift_log)}")

    axiom_encrypted, shared_log = encrypt_1to1(encrypted)
    log_debug(f"[ENCRYPT] AxiomCore result: {axiom_encrypted}")

    # === Injecting Boundary Blur Logic (B2.4) ===
    encrypted, blur_triggered = inject_boundary_blur(encrypted, shift_log)
    if (blur_triggered):
        log_debug("[BLUR] Boundary Blur Logic activated: fallback logic applied to midpoint.")
 
    # === Injecting Quantum Foam Drift ===
    foam_array = generate_planck_noise(key, length=len(encrypted))
    encrypted = ''.join([
        apply_quantum_foam_shift(c, shift_log[i], foam_array, i)
        for i, c in enumerate(encrypted)
    ])
    log_debug(f"[QUANTUM FOAM] Applied quantum drift to {len(encrypted)} characters.")
    oracle_output.config(state='normal')
    oracle_output.insert(tk.END, f"Quantum Foam Drift: ACTIVE (intensity={FOAM_INTENSITY}, stability={FOAM_STABILITY})\n")
    oracle_output.config(state='disabled')

    # === Injecting Fractal Memory Drift (B3.2) with Drift Decay ===
    memory = log_fractal_memory(encrypted, shift_log)
    memory = decay_fractal_memory(memory, mode="wobble", strength=0.1)
    encrypted = apply_fractal_shift(encrypted, memory)

    # === Visual Drift Bar Output ===
    drift_bar = ''.join(['|' if s > 40 else ':' if s > 20 else '.' for s in memory['shift_log']])
    entropy_value = memory['entropy_score']
    drift_score = calculate_drift_score(entropy=entropy_value, shift_log=memory['shift_log'])
        # Colorize label based on drift score
    if (drift_score > 75):
        drift_color = "red"
    elif (drift_score > 40):
        drift_color = "orange"
    else:
        drift_color = "green"

    entropy_drift_label.config(
        text=f"Entropy: {entropy_value} | Drift: {drift_score} | Drift Bar: {drift_bar[:30]}",
        foreground=drift_color
    )

 # === Store memory snapshot into parasite_memory.json ===
    memory_snapshot = {
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
        "entropy": memory["entropy_score"],
        "shift_log": [int(s) for s in memory["shift_log"]],
    "bias": [int(b) for b in memory["position_bias"]]
    }
    parasite_mem = load_parasite_memory()
    parasite_mem.setdefault("fractal_history", []).append(memory_snapshot)
    if (len(parasite_mem["fractal_history"]) > 20):
        parasite_mem["fractal_history"] = parasite_mem["fractal_history"][-20:]
    with open("parasite_memory.json", "w") as f:
        json.dump(parasite_mem, f, indent=4)

    # === Visual Drift Bar Output ===
    print("Fractal Drift Signature:")
    drift_bar = ''.join(['|' if s > 40 else ':' if s > 20 else '.' for s in memory['shift_log']])
    print(drift_bar)
    print(f"Entropy: {memory['entropy_score']}")
    print(f"Sample Bias: {memory['position_bias'][:10]}")
    log_debug(f"[FRACTAL DRIFT] {drift_bar}")
    log_debug(f"[ENCRYPT] AxiomCore word count: {len(axiom_encrypted.split())}")

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, axiom_encrypted)

    key_profile = analyze_key(key)
    log_debug(f"[KEY PROFILE] {key_profile}")

    subconscious_log = generate_subconscious_log(message, key, shift_log)

    entropy_value = sum(ord(c) for c in message)
    drift_score = calculate_drift_score(entropy=entropy_value, shift_log=shift_log)
    parasite_memory = update_parasite_memory(drift_score, entropy_value)
    fib_mod += parasite_memory["drift_bias"]
    cube_mod += parasite_memory["drift_bias"]
    shift_mod += parasite_memory["drift_bias"]
    oracle_entry = {
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
        "entropy": entropy_value,
        "vowel_count": sum(1 for c in key if c.lower() in 'aeiou'),
        "branches": key_profile["branch_path"],
        "drift_score": drift_score,
        "flip_triggered": any("flip" in tag.lower() for tag in subconscious_log),
        "subconscious_tags": subconscious_log,
        "oracle_state": oracle_bias["state"],
        "oracle_response": oracle_bias["response"]
    }
    oracle_memory["runs"].append(oracle_entry)
    with open("oracle_memory.json", "w") as f:
        json.dump(oracle_memory, f, indent=4)
    oracle_output.config(state='normal')
    oracle_output.delete("1.0", tk.END)
    oracle_output.insert(tk.END, f"Oracle State: {oracle_bias.get('simulated_state', oracle_bias['state'])}\n")
    oracle_output.insert(tk.END, f"Oracle Response: {oracle_bias.get('simulated_response', oracle_bias['response'])}\n")
    oracle_output.insert(tk.END, f"Drift Score: {drift_score}\n")
    oracle_output.insert(tk.END, f"Entropy: {entropy_value}\n")
    oracle_output.insert(tk.END, f"Subconscious Tags: {', '.join(subconscious_log)}\n")
    oracle_output.insert(tk.END, f"Parasite Influence: {parasite_memory['drift_bias']} (across {parasite_memory['influence_count']} runs)\n")


    oracle_output.config(state='disabled')



    package = {
        "cipher": axiom_encrypted,
        "shift_log": [int(s) for s in shift_log],
        "shared_symbols": shared_log,
        "key_hash": hashlib.sha256(key.encode()).hexdigest(),
        "created_at": time.ctime(),
        "key_profile": key_profile,
        "subconscious": subconscious_log
    }

    # === Encrypt and HMAC the .bhex package ===
    package_bytes = json.dumps(package).encode()
    aes_key = hashlib.sha256(key.encode()).digest()
    iv, encrypted_package = encrypt_aes(package_bytes, aes_key)
    hmac_signature = generate_hmac(encrypted_package, aes_key)

    secure_package = {
        "iv": base64.b64encode(iv).decode(),
        "cipher": base64.b64encode(encrypted_package).decode(),
        "hmac": base64.b64encode(hmac_signature).decode()
    }

    filename = f"blackhole_{time.strftime('%Y-%m-%d_%H-%M-%S')}.bhex"
    with open(filename, "w") as f:
        json.dump(secure_package, f)
    log_debug(f"[ENCRYPT] .bhex package saved: {filename}")

    with open("encrypted_output.bhex", "w") as f:
        json.dump(secure_package, f)
    log_debug("[ENCRYPT] Backup package saved: encrypted_output.bhex")

    root.config(cursor="")

def decrypt():
    global current_package
    root.config(cursor="watch")
    root.update()

    file_path = filedialog.askopenfilename(
        title="Select .bhex File (or Cancel for default)",
        filetypes=[("BlackHole Package", "*.bhex")]
    )

    if (file_path):
        try:
            with open(file_path, "r") as f:
                current_package = json.load(f)
            log_debug(f"[DECRYPT] Loaded .bhex package from {file_path}")
        except Exception as e:
            messagebox.showerror("❌ Error", f"Failed to load selected .bhex: {e}")
            return
    else:
        try:
            with open("encrypted_output.bhex", "r") as f:
                current_package = json.load(f)
            log_debug("[DECRYPT] Loaded fallback encrypted_output.bhex")
        except Exception as e:
            messagebox.showerror("❌ Error", f"No .bhex file selected and fallback failed: {e}")
            return

    try:
        iv = base64.b64decode(current_package['iv'])
        cipher_data = base64.b64decode(current_package['cipher'])
        received_hmac = base64.b64decode(current_package['hmac'])

        password = simpledialog.askstring("🔐 Password", "Enter password to decrypt:", show='*', parent=root)
        if (not password):
            messagebox.showerror("❌ Error", "Password is required.")
            return

        aes_key = hashlib.sha256(password.encode()).digest()

        if (not verify_hmac(cipher_data, aes_key, received_hmac)):
            messagebox.showerror("⚠️ Integrity Error", "HMAC verification failed. The file may have been tampered with.")
            return

        decrypted_package = json.loads(decrypt_aes(cipher_data, aes_key, iv).decode())

        cipher = decrypted_package.get("cipher", "")
        shift_log = decrypted_package.get("shift_log", [])
        shared_log = decrypted_package.get("shared_symbols", [])
        current_package = decrypted_package

    except Exception as e:
        messagebox.showerror("❌ Error", f"Failed to decode encrypted .bhex: {e}")
        return

    if (not cipher):
        messagebox.showwarning("⚠️ Warning", "Cipher text is empty.")
        return

    log_debug("[DECRYPT] Starting AxiomCore symbol decryption.")
    try:
        blackhole_ready_text = decrypt_1to1(cipher)
        log_debug(f"[DECRYPT] AxiomCore output: {blackhole_ready_text}")
    except Exception as e:
        log_debug(f"[DECRYPT] AxiomCore failed: {e}")
        messagebox.showerror("❌ Error", "AxiomCore decryption failed.")
        return

    #  Enforce length uniformity for shift_log and message
    if (len(blackhole_ready_text) != len(shift_log)):
        min_len = min(len(blackhole_ready_text), len(shift_log))
        blackhole_ready_text = blackhole_ready_text[:min_len]
        shift_log = shift_log[:min_len]

    decrypted = decrypt_message(blackhole_ready_text, shift_log)
    log_debug(f"[DECRYPT] Final result: {decrypted}")

    output_text.delete("1.0", tk.END)
    decrypted = convert_words_to_numbers(decrypted)
    output_text.insert(tk.END, decrypted)
    root.config(cursor="")

def convert_numbers_to_words(text):
    result = []
    i = 0
    num_to_word = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    while (i < len(text)):
        if (text[i].isdigit()):
            word = num_to_word[text[i]]
            result.append(f"__{word}__")
        else:
            result.append(text[i])
        i += 1
    return ''.join(result)

def convert_words_to_numbers(text):
    word_to_num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    result = []
    parts = text.split('__')
    for part in parts:
        if (part in word_to_num):
            result.append(word_to_num[part])
        else:
            result.append(part)
    return ''.join(result)

def setup_gui():
    global entropy_drift_label
    global root, input_text, output_text

    root = ttk.Window(themename="cyborg")
    root.title("🕳️ BLACKHOLE OS – V6")
    root.geometry("900x700")

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill='both', expand=True)

    input_label = ttk.Label(frame, text="Enter Message:", font=("Helvetica", 12))
    input_label.grid(row=0, column=0, sticky="w", pady=5)
    input_text = ttk.ScrolledText(frame, width=90, height=6)
    input_text.grid(row=1, column=0, columnspan=5, pady=5)

    output_label = ttk.Label(frame, text="Output:", font=("Helvetica", 12))
    output_label.grid(row=2, column=0, sticky="w", pady=5)
    output_text = ttk.ScrolledText(frame, width=90, height=6)
    output_text.grid(row=3, column=0, columnspan=5, pady=5)

    oracle_label = ttk.Label(frame, text="Oracle Insight:", font=("Helvetica", 12))
    oracle_label.grid(row=6, column=0, sticky="w", pady=5)
    oracle_text = ttk.ScrolledText(frame, width=90, height=6, state='disabled')

    entropy_drift_label = ttk.Label(frame, text="Entropy: -- | Drift: --", font=("Helvetica", 10), foreground="cyan")
    entropy_drift_label.grid(row=8, column=0, columnspan=5, sticky="w", pady=5)
    oracle_text.grid(row=7, column=0, columnspan=5, pady=5)

    global oracle_output
    oracle_output = oracle_text

    ttk.Button(frame, text="Encrypt", width=18, command=encrypt, bootstyle=SUCCESS).grid(row=4, column=0, pady=10, padx=5)
    ttk.Button(frame, text="Decrypt", width=18, command=decrypt, bootstyle=INFO).grid(row=4, column=1, pady=10, padx=5)
    ttk.Button(frame, text="Copy Output", width=18, command=lambda: pyperclip.copy(output_text.get("1.0", tk.END).strip()), bootstyle=PRIMARY).grid(row=5, column=0, pady=5, padx=5)
    ttk.Button(frame, text="Paste Input", width=18, command=lambda: input_text.insert(tk.END, pyperclip.paste()), bootstyle=WARNING).grid(row=5, column=1, pady=5, padx=5)
    ttk.Button(frame, text="Load .bhex File", width=18, command=decrypt, bootstyle=SECONDARY).grid(row=5, column=2, pady=5, padx=5)

    root.mainloop()

setup_gui()