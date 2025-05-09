# main.py
"""
BlackHole Launcher Script
This script allows CLI-based encryption and decryption of messages using the V6 engine.
"""

import argparse
from src import blackhole_v6

parser = argparse.ArgumentParser(description="BlackHole Encryption CLI Tool")
parser.add_argument('--mode', choices=['encrypt', 'decrypt'], required=True, help="Mode to run: encrypt or decrypt")
parser.add_argument('--message', type=str, help="Plaintext or .bhex file path depending on mode")
parser.add_argument('--password', type=str, required=True, help="Password for encryption/decryption")

args = parser.parse_args()

if args.mode == 'encrypt':
    result = blackhole_v6.encrypt_message(args.message, args.password)
    print("\n[Encrypted Output]\n", result)

elif args.mode == 'decrypt':
    with open(args.message, 'r') as f:
        bhex_data = f.read()
    result = blackhole_v6.decrypt_message(bhex_data, args.password)
    print("\n[Decrypted Output]\n", result)