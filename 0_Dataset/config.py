# central definition of project wide uses constant
import os

DATASET_ROOT_FOLDER = os.path.abspath("../0_Dataset/")

# Root directory of the dataset with manuell selected images
# in two classes
# - with_seamounts
# - without_seamounts
DATASETS_SOURCE_FOLDER = os.path.join(DATASET_ROOT_FOLDER, "raw_dataset")
# Categories as subfolders in `image_folder`  
CATEGORIES = ["with_seamount", "without_seamount"]  

# Folder for cropped and shrinked images
DATASETS_FOLDER = os.path.join(DATASET_ROOT_FOLDER, "processed_data")

IMAGE_SIZE = (128, 128)  # Image dimensions for the model
CROP_PIXELS = 70  # Pixels to crop from each border