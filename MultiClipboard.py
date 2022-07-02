import sys
import json
import clipboard

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_items(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        return data
    

if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)
    
    if command == "save":
        pass
    elif command == "load":
        pass
    elif command == "list":
        pass
    else:
        print("Unknown Command.")
else:
    print("Only one command accepted.")