import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to the folder containing new, unlabeled images
test_image_dir = "../path_to_unlabeled_images"  # Update with the correct path

# Image size should match the one used during training (256x256)
IMAGE_SIZE = (256, 256)

# Function to load and preprocess the image
def load_and_preprocess_image(image_path):
    # Load the image in color (BGR format)
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    # Convert to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Resize the image to the required input size
    image_resized = cv2.resize(image, IMAGE_SIZE)
    # Normalize the pixel values to [0, 1]
    image_resized = image_resized / 255.0
    # Add batch dimension (1 image)
    image_resized = np.expand_dims(image_resized, axis=0)
    return image_resized

# Function to visualize the image and its predicted bounding box
def visualize_prediction(image, pred_bbox):
    # Get the image dimensions
    h, w, _ = image.shape

    # Convert predicted bounding box from normalized to pixel values
    x_min, y_min, x_max, y_max = pred_bbox
    x_min = int(x_min * w)
    y_min = int(y_min * h)
    x_max = int(x_max * w)
    y_max = int(y_max * h)

    # Plot the image
    plt.imshow(image)
    # Draw the predicted bounding box
    plt.gca().add_patch(plt.Rectangle(
        (x_min, y_min), x_max - x_min, y_max - y_min,
        edgecolor='red', facecolor='none', lw=2, label='Predicted'
    ))
    plt.legend()
    plt.show()

# Load all images from the test directory
test_images = []
image_names = []

for image_name in os.listdir(test_image_dir):
    image_path = os.path.join(test_image_dir, image_name)
    if image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        test_images.append(image_path)
        image_names.append(image_name)

# Iterate over the test images and make predictions
for image_path, image_name in zip(test_images, image_names):
    # Load and preprocess the image
    image = load_and_preprocess_image(image_path)
    
    # Predict the bounding box using the trained model
    pred_bbox = model.predict(image)[0]  # Model returns a batch of predictions, we take the first one

    # Visualize the prediction
    original_image = cv2.imread(image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    visualize_prediction(original_image, pred_bbox)

    print(f"Predicted bounding box for {image_name}: {pred_bbox}")
