1. Handling Images with No Seamount (Empty Bounding Boxes)

If there are images in the dataset that do not contain a seamount, the ground truth bounding box for such images would ideally be [0, 0, 0, 0], representing no object. In such cases:

    The model should learn to predict [0, 0, 0, 0] for images that do not contain a seamount.
    You could make sure that such cases are properly represented in your dataset by ensuring that non-object images have their bounding boxes set to [0, 0, 0, 0].
