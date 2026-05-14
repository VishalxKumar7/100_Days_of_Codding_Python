import json

with open("browser.json", "r") as f:
    data = json.load(f)

# Fix the \u001a character
data["x-goog-authuser"] = "0"

with open("browser.json", "w") as f:
    json.dump(data, f, indent=4)

print("Fixed!")
print(data.keys())