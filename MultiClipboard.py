import sys
import json
import clipboard

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def update_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

if len(sys.argv) == 2:
    data = load_data(SAVED_DATA)
    command = sys.argv[1]
    print(command)
    
    if command == "save":
        key = input("Enter Key >> ")
        if key not in data:
            data[key] = clipboard.paste()
            save_data(SAVED_DATA, data)
            print(f"Clipboard has been saved with the key {key}.")
        else:
            print(f"The key {key} already exists.")
    elif command == "load":
        key = input("Enter Key >> ")
        if key in data:
            clipboard.copy(data[key])
            print(f"Copied data.")
        else:
            print(f"The key {key} does not exist.")
    elif command == "list":
        for i in data:
            print(f"{i}: {data[i]}")
    elif command == "delete":
        key = input("Enter Key >> ")
        if key in data:
            data.pop(key, None)
            save_data(SAVED_DATA, data)
            print(f"Removed value with key {key}.")
    else:
        print("Unknown Command.")
else:
    print("Only one command accepted.")