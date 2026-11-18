# Password Checker 🔐

A simple Python script to check if a password is strong or weak, with a web interface built using Gradio.

I built this while learning Ethical Hacking. It helps users create stronger passwords.

## Try It On Your Phone (No Installation)

You can test the script directly from your phone using this Gradio link:

**Demo Link:** https://842a73b33f39824ff8.gradio.live
*This is a temporary link*

Just open the link on your phone browser and test a password.

## What It Checks
This version checks only 4 things:

- ✅ Password length
- ✅ Uppercase letters (A-Z)
- ✅ Numbers (0-9)
- ✅ Special symbols (! @ # $ %)

It does NOT check for lowercase letters in this version.

## How To Use

### Option 1: Use the Gradio Link (Easiest)
1. Open the Gradio link above on your phone
2. Type a password
3. See your result

### Option 2: Run It Yourself
```bash
pip install gradio
python password_checker.py
