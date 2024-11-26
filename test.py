import json

try:
    with open('D:\Jarvis\engine\cookies.json', 'r') as f:
        api_data = json.load(f)
        print("API Key:", api_data.get("api_key", "Key not found"))
except Exception as e:
    print("Error reading JSON file:", e)
