# Workflow for Seamount Image Processing

```mermaid
graph TD
    A[Download Images - Seg_Step1] -->|Images defined by seamounts.csv| B[Save in seamounts_bboxes]
    A -->|Generate bounding box coordinates| C[Save seamounts_bboxes.csv]
    B --> D[Download Larger Standardized Tiles - Seg_Step2]
    D -->|File names from seamounts_bboxes| E[Save in seamounts_galore]
    E --> F[Preprocess Images - Seg_Step3]
    F -->|Crop seamounts_galore| G[Save in seamounts_galore_cropped]
    F -->|Crop seamounts_bboxes| H[Save in seamounts_bboxes_cropped]
    F -->|Find images in seamounts_galore_cropped| I[Create bounding box overlays in marked_images]
    I -->|Generate pixel coordinates| J[Save output_pixel_coordinates.csv]
    J --> K[Sorting and Optional Deleting of Doubles]
    K --> L[Load Standard Tiles - Step 5]
    L -->|Manually Sorted Tiles| M[Save in seamounts_seg]
    M --> N[Merge and Clean Up CSV Files - Step 6]
    N -->|Input: merge_pixel_coordinates_csvs| O[Output: merged_pixel_coordinates.csv]
    O -->|Indicates Missing Rows| P[Hunt Missing Entries - Seg_Step7]
    P -->|Download Images Again| Q[Back to Step 1]
    Q -->|Processing the Missing| D

    %% Highlight important outputs
    style M fill:#FFD700,stroke:#000,stroke-width:2px, color:#000
    style O fill:#FFD700,stroke:#000,stroke-width:2px, color:#000

    %% New additions for Model Building
    M --> R[Model Building]
    O --> R[Model Building]

    %% Move "Model Building" to the bottom and make it larger
    style R fill:#ff6347,stroke:#000,stroke-width:4px, font-size:20px
    subgraph " "
        direction TB
        R
    end



```
1st step: A specified number of images is downloaded by the script "Seg_Step1". These images are defined by the position and covered area stated in `seamounts.csv` (so they contain zoomed-in images focused on the seamount based on the area stated in km²). These images are saved in "seamounts_bboxes" and produce a `seamounts_bboxes.csv` file with the bounding box geographical coordinates. (Note: This is not sufficient for Image Segmentation, as Image Segmentation needs pixel coordinates.)

2nd step: The script "Seg_Step2" downloads larger, standardized tiles (60nm x 60nm) based on the file names contained in `seamounts_bboxes` and saves them in the folder "seamounts_galore".

3rd step: The preprocessing part of the script "Seg_Step3" crops the images from "seamounts_galore" and "seamounts_bboxes" (Note: The folders have to be specified, and the script must be executed twice for this to happen). The cropped files are saved in "seamounts_galore_cropped" and "seamounts_bboxes_cropped", respectively.

4th step: The main part of "Seg_Step3" creates images with bounding box overlays in the folder "marked_images" by finding the images in "seamounts_bboxes_cropped" within the images in "seamounts_galore_cropped". It also produces an `output_pixel_coordinates.csv` file for later use in Image Segmentation.

Step 5: Sorting and (optional) delete any doubles. Step 5: Load standard tiles for the manually sorted tiles. These are stored in "seamounts_seg".

Step 6: merge and clean up .csv files. The input folder for this is "merge_pixel_coordinates_csvs" and the output file is: "merged_pixel_coordinates.csv" If rows are missing it is indicated in the output.

Step 7 is hunting missing entries if applicable. "Seg_Step7" downloads these images again (like in step 1) from there on an arrow named "processing the missing" should again go to step 2.

```mermaid
graph TD
    %% Start with Model Building at the top
    R[Model Building]

    %% Add arrows from Model Building to the two new models
    R -->|Standalone Model| S[objdet_standalone_model_1_0]
    R -->|Transfer with ResNet50| T[objdet_transfer_with_ResNet50_model_1_0]

    %% Style for Model Building
    style R fill:#ff6347,stroke:#000,stroke-width:4px, font-size:20px

    %% Style for the new models with black text
    style S fill:#87CEEB,stroke:#000,stroke-width:2px, color:#000
    style T fill:#87CEEB,stroke:#000,stroke-width:2px, color:#000

    %% Add the next model and comment for objdet_standalone_model_1_1
    S -->|added capability to classify no_seamount| U[objdet_standalone_model_1_1*]
    
    %% Comment for objdet_standalone_model_1_1
    classDef comment fill:#f8f8f8,stroke:none;
    class U comment;
    
    %% Style for objdet_standalone_model_1_1
    style U fill:#87CEEB,stroke:#000,stroke-width:2px, color:#000
    U:::comment

    %% Add downward arrow to objdet_standalone_model_1_2 with text
    U -->|added keras tuner| V[objdet_standalone_model_1_2**]

    %% Style for objdet_standalone_model_1_2
    style V fill:#87CEEB,stroke:#000,stroke-width:2px, color:#000

    %% Add rightward arrow to objdet_transfer_with_MobileNetV2_model_1_1***
    U -->|added transfer with MobileNetV2| W[objdet_transfer_with_MobileNetV2_model_1_1***]

    %% Style for objdet_transfer_with_MobileNetV2_model_1_1***
    style W fill:#87CEEB,stroke:#000,stroke-width:2px, color:#000

```
\* Steps in Hyperparameter-Tuning:
- Higher resolution: no significant positive change

- Higher Batch size(32): Takes a lot longer, not significantly better, validation MAE a bit better

- back to batch size 16

- Smaller learning rate(0.0001): worse

- higher learning rate(0.01): Takes very long. Doesn't work at all.

- learning rate scheduler: no positive change

- batch normalization: Takes longer, weird results, cannot really interpret if it's good or not, but bounding box prediction seems to be worse (lot more 0 IoUs)

- more complex model: Of course takes longer, visibly better results with a positive impact especially on the IoU. Best model so far
Changes Summary for this step:

    Convolutional Layers: Added more convolutional layers (256 and 512 filters).
    Fully Connected Layers: Added two fully connected layers (1024 and 512 units) for deeper decision-making.
    MaxPooling Layers: Max pooling layers were added after each convolution to reduce spatial dimensions.
    Dropout Layers: Added additional dropout layers to help prevent overfitting.

- k-fold cross validation: Failed with batch size 16 due to GPU ressource error (is already on best GPU environment available to me). Try with batch size 8 also ressource exhausted. Try with image size 128x128, runs, results not significantly better but could be explored further.

- when trying to revert to previous model configuration I noticed that while the code text can be exactly the same, the model can be built entirely different, like here:![alt text](image.png)

- after copying the previous .ipynb from the git history I did not have this problem again, maybe there was something different in the script after all.

- kept status quo as version 1_1 and continued exploration on version 1_2

\*\*

- keras tuner: Does it only run 2 epochs? If yes then loss will still be very high, does that make sense? First trial hyperband:2 max:100 interrupted due to error RAM again.Reduced image size (128x128). Reduced batch size (8). Custom data generator for loading images in batches. Limited the hyperparameter search space to reduce memory consumption. Clearing the Keras session after training to release memory. Now it runs, but this runs forever... after the first 100 iterations (~45min) it switches from 2 to 4 epochs. Aborted, takes too long and uncertain output (due to image size reduction or ending in an error after running 12h, etc.) Probably is a powerful tool but takes too long to just let it run, maybe explore later within very specific bounds so that it doesn't try everything but only certain hyperparameters?

- even more layers?: tried once, had worse results

- Attention Mechanism: Add an attention layer (e.g., SEBlock or Spatial Attention):

- L2 Regularization:

- Non-Maximum Suppression (NMS):

- Image augmentation (in images with object it would need to modify the box as well, this I didn't manage so far)

- In other models: Ensemble Models, Transfer Learning, Model that can output more than one seamount.

\*\*\*

- MobileNetV2, integration of this Transfer Learning strategy had worse results than the standalone model, maybe could be tweaked

- ResNet50 produced memory error first and then Kernel and program crashes, so abandoned

- maybe transfer learning with normal image recognition models is not so easily applicable to topographical/bathygraphical data