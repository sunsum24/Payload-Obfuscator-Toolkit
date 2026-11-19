import base64
import codecs
import argparse
import sys

def base64_encode(payload):
    """Encodes payload in Base64."""
    encoded = base64.b64encode(payload.encode()).decode()
    return f"powershell -enc {encoded}"

def hex_encode(payload):
    """Converts payload to a Hex string format (useful for shellcode)."""
    hex_string = ''.join(f'\\x{ord(c):02x}' for c in payload)
    return hex_string

def rot13_encode(payload):
    """Applies a simple ROT13 cipher to the payload."""
    return codecs.encode(payload, 'rot_13')

def main():
    parser = argparse.ArgumentParser(description="Red Team Payload Obfuscator")
    parser.add_argument("-p", "--payload", required=True, help="The raw command or payload to obfuscate")
    parser.add_argument("-t", "--type", choices=['base64', 'hex', 'rot13'], required=True, help="Obfuscation type")
    
    args = parser.parse_args()
    
    print(f"[*] Original Payload: {args.payload}")
    print(f"[*] Obfuscation Method: {args.type.upper()}\n")
    
    if args.type == 'base64':
        result = base64_encode(args.payload)
        print(f"[+] Obfuscated Output (Run in PowerShell):\n{result}")
        
    elif args.type == 'hex':
        result = hex_encode(args.payload)
        print(f"[+] Obfuscated Output (Hex):\n{result}")
        
    elif args.type == 'rot13':
        result = rot13_encode(args.payload)
        print(f"[+] Obfuscated Output (ROT13):\n{result}")

if __name__ == "__main__":
    print("⚠️ WARNING: This tool is for authorized Red Team engagements and educational purposes only.")
    main()
