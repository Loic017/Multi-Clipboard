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

if len(sys.argv) == 2:
    data = load_data(SAVED_DATA)
    command = sys.argv[1]
    print(command)
    
    if command == "save":
        key = input("Enter Key >> ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
    elif command == "load":
        #key = input("Enter Key")
        #clipboard.copy(key)
        pass
    elif command == "list":
        pass
    else:
        print("Unknown Command.")
else:
    print("Only one command accepted.")