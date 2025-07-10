from deepface import DeepFace
import os
import json

# Load cricketer data
with open("cricketers.json", "r") as file:
    cricketers = json.load(file)

# Folder with known images
img_folder = "images"
input_img = "test.jpg"  # Replace this with the actual test image

# Initialize result
best_match = None
min_distance = float("inf")

# Compare with each known image
for filename in os.listdir(img_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        try:
            result = DeepFace.verify(
                img1_path=os.path.join(img_folder, filename),
                img2_path=input_img,
                model_name='VGG-Face',
                enforce_detection=False
            )
            if result["verified"] and result["distance"] < min_distance:
                min_distance = result["distance"]
                best_match = filename.split(".")[0]
        except Exception as e:
            print(f"Error comparing with {filename}: {e}")

# Display result
if best_match:
    print(f"\n🎯 Match Found: {best_match.replace('_', ' ')}")
    print(f"📌 Team: {cricketers[best_match]['team']}")
    print(f"🧠 Role: {cricketers[best_match]['role']}")
    print(f"📌 Jersey No.: {cricketers[best_match]['jersey no.']}")
    print(f"📌 Style: {cricketers[best_match]['batting_style']}")
    print(f"📝 Bio: {cricketers[best_match]['bio']}")
else:
    print("❌ No matching cricketer found.")
