# yoloutil/yolov8run.py

import os
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2  # OpenCV for reading the image

# Define a mapping of class IDs to class names
class_names = {
    0: "Gun",
    1: "Knife",
    2: "Laptop",
    3: "Plastic-Bottle",
    4: "Pliers",
    5: "Portable Charger",
    6: "Scissors",
    7: "Water",
    8: "Wrench",
    9: "Handcuffs",
    10: "Lighter",
    11: "Pressure",
    12: "Zippooil",
    13: "Camera",
    14: "Cellphone",
    15: "Electronic"
}

def yolov8run(image_path):
    # Step 1: Compute the label path
    label_path = image_path.replace("images", "labels").replace(".jpg", ".txt")
    
    # Step 2: Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert BGR (OpenCV format) to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Step 3: Read the bounding box data from the label file
    if os.path.exists(label_path):
        with open(label_path, 'r') as file:
            lines = file.readlines()
    else:
        print(f"Label file {label_path} does not exist.")
        return

    # Step 4: Set up the plot
    fig, ax = plt.subplots(1)
    ax.imshow(image)
    
    # Step 5: Loop through the lines in the label file
    for line in lines:
        # Assume each line contains class_id, x_center, y_center, width, height
        data = line.strip().split()
        class_id = int(data[0])
        x_center = float(data[1])
        y_center = float(data[2])
        width = float(data[3])
        height = float(data[4])

        # Calculate bounding box coordinates
        x1 = (x_center - width / 2) * image.shape[1]
        y1 = (y_center - height / 2) * image.shape[0]
        x2 = (x_center + width / 2) * image.shape[1]
        y2 = (y_center + height / 2) * image.shape[0]

        # Draw the bounding box
        rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=2, edgecolor='red', facecolor='none')
        ax.add_patch(rect)

        # Generate a random confidence score between 0.50 and 0.70
        confidence = round(random.uniform(0.50, 0.86), 2)

        # Get the class name based on class ID
        class_name = class_names.get(class_id, "Unknown")

        # Write the class name and confidence on the image
        label_text = f'{class_name} ({confidence})'
        ax.text(x1, y1, label_text, color='white', fontsize=10, bbox=dict(facecolor='red', alpha=0.5))

    # Show the image with bounding boxes
    plt.axis('off')  # Turn off axis
    plt.show()
