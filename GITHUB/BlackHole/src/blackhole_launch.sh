#!/bin/bash
echo "🌀 BlackHole V6 Launcher"
read -p "Enter mode (encrypt/decrypt): " mode
read -p "Enter message or path to .bhex file: " message
read -s -p "Enter password: " password
echo

python main.py --mode "$mode" --message "$message" --password "$password"

