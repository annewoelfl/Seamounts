import os
import pandas as pd

# Paths
image_dir_without_objects = "/content/no_objects"  # Folder with images without objects
csv_path = "/content/merged_pixel_coordinates.csv"  # Path to the CSV file

# Load the existing CSV file
bbox_data = pd.read_csv(csv_path)

# Get a list of images in the folder without objects
no_object_images = [img for img in os.listdir(image_dir_without_objects) if img.endswith(('.png', '.jpg', '.jpeg'))]

# Create new entries for images without objects
new_entries = []
for img_name in no_object_images:
    new_entries.append({
        "image_name": img_name,
        "x_min": -1,
        "y_min": -1,
        "x_max": -1,
        "y_max": -1
    })

# Convert the new entries to a DataFrame
new_entries_df = pd.DataFrame(new_entries)

# Append the new entries to the existing DataFrame
updated_bbox_data = pd.concat([bbox_data, new_entries_df], ignore_index=True)

# Save the updated CSV file
updated_bbox_data.to_csv(csv_path, index=False)
print(f"Updated CSV file saved to {csv_path}")
