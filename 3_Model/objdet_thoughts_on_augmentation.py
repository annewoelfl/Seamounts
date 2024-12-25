from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import random
import cv2

# Custom Data Generator for applying augmentations to both images and bounding boxes
class BBoxImageDataGenerator:
    def __init__(self, image_datagen, bbox_datagen, image_size=(256, 256)):
        self.image_datagen = image_datagen
        self.bbox_datagen = bbox_datagen
        self.image_size = image_size
    
    def flow(self, images, bboxes, batch_size=32, shuffle=True):
        """
        Custom generator that applies image augmentations and updates bounding boxes.
        """
        while True:
            # Shuffle images and bounding boxes together if needed
            if shuffle:
                indices = np.random.permutation(len(images))
                images = images[indices]
                bboxes = bboxes[indices]
            
            for start in range(0, len(images), batch_size):
                # Get the batch of images and bounding boxes
                end = min(start + batch_size, len(images))
                batch_images = images[start:end]
                batch_bboxes = bboxes[start:end]
                
                augmented_images = []
                augmented_bboxes = []
                
                for i in range(len(batch_images)):
                    image = batch_images[i]
                    bbox = batch_bboxes[i]
                    
                    # Apply augmentations to both image and bbox
                    augmented_image, augmented_bbox = self.apply_augmentation(image, bbox)
                    
                    augmented_images.append(augmented_image)
                    augmented_bboxes.append(augmented_bbox)
                
                yield np.array(augmented_images), np.array(augmented_bboxes)
    
    def apply_augmentation(self, image, bbox):
        """
        Applies a random set of augmentations to the image and bounding box.
        """
        # Random horizontal flip
        if random.random() > 0.5:
            image = np.fliplr(image)
            bbox = flip_bbox_horizontally(bbox, image.shape[1])
        
        # Random vertical flip
        if random.random() > 0.5:
            image = np.flipud(image)
            bbox = flip_bbox_vertically(bbox, image.shape[0])
        
        # Random rotation (apply a random angle between -30 and 30 degrees)
        angle = random.uniform(-30, 30)
        image = self.rotate_image(image, angle)
        bbox = rotate_bbox(bbox, angle, image.shape[1], image.shape[0])
        
        # Random translation (shift image randomly)
        tx, ty = random.randint(-10, 10), random.randint(-10, 10)
        image = self.translate_image(image, tx, ty)
        bbox = translate_bbox(bbox, tx, ty)
        
        # Random scaling
        scale_x = random.uniform(0.8, 1.2)
        scale_y = random.uniform(0.8, 1.2)
        image = self.scale_image(image, scale_x, scale_y)
        bbox = scale_bbox(bbox, scale_x, scale_y)
        
        # Resize image to desired size
        image = cv2.resize(image, self.image_size)
        
        return image, bbox
    
    def rotate_image(self, image, angle):
        """Rotate image by the given angle."""
        h, w = image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(image, M, (w, h))
        return rotated_image
    
    def translate_image(self, image, tx, ty):
        """Translate the image by tx, ty pixels."""
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
        return translated_image
    
    def scale_image(self, image, scale_x, scale_y):
        """Scale the image by scale_x and scale_y."""
        h, w = image.shape[:2]
        scaled_image = cv2.resize(image, (int(w * scale_x), int(h * scale_y)))
        return scaled_image

# Example usage
image_datagen = ImageDataGenerator()  # No augmentation for images
bbox_datagen = BBoxImageDataGenerator(image_datagen, image_size=(256, 256))

# Assuming `images` is a numpy array of shape (num_images, height, width, channels)
# and `bboxes` is a numpy array of shape (num_images, 4) containing [x_min, y_min, x_max, y_max] for each image
# You'd call bbox_datagen.flow to get batches of augmented images and bounding boxes:
# generator = bbox_datagen.flow(images, bboxes, batch_size=32)

