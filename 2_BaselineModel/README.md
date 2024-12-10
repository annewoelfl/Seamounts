# Baseline Model

**[Notebook](baseline_model.ipynb)**

1. **Introduction and data choice**: First trials of a base model were done before we settled on a final way of preparing the data. Several possibilities were regarded:
   - using only hand-selected examples of positive/negative examples (e.g. from a certain area)
   - using a lot of automatically downloaded images according to a seamount database worldwide.
   - using only high-resolution bathymetric data or also low.
While high resolution data was preferred, it only existed as asymmetric, diagonal strips of imagery across an otherwise empty or low-resolutioned picture. We settled for high-res data with the low-res "background" parts still in place, as it was easy to generate and seemed quite fluent in the image data (avoiding too much contrast, which has no meaning in the sense of the project).

2. **Baseline Model**: While first trials were actually made with a simple CNN, we settled for a simple logistic regression and, as an alternative, for a random forest model to serve as our baseline approach.

3. **Model Definition and Evaluation**: Exemplary I will here present the results of running the baseline models on a set of ~2500 seamount images generated according to a database of seamounts (https://data.unep-wcmc.org/datasets/41) and ~1000 non_seamount images. This imbalance was adressed with undersampling the majority class. Further the images were cropped (to erase border and watermark), resized and normalized. Logistic Regression was trained on the undersampled training set and evaluated using accuracy, precision, recall, F1-score, and visualizations.
   - Evaluation of Logistic Regression: The model performed well on the "with_seamount" class but struggled with the "without_seamount" class, as seen in lower precision. Validation accuracy (89%) was higher than test accuracy (86%), indicating potential overfitting.
   - Evaluation of Random Forest: Validation Results: Evaluated the model using classification metrics (accuracy_score, classification_report) on both validation and test sets. The model achieves excellent performance with 99% accuracy, showing high precision and recall for both categories (with and without seamount). The macro and weighted averages for precision, recall, and f1-score are also very high, which is a good indication of balanced performance across both classes. Similar performance is observed in the test set, with an accuracy of 99% and nearly identical precision, recall, and f1-scores across both classes. This suggests that the model generalizes well to unseen data.

5. **Results/Learnings for the rest of the project**:
   - Results: The Logistic Regression model's precision and recall varied between classes, with high recall for "without_seamount" but lower recall for "with_seamount". Overall accuracy was decent but suggests the model could benefit from improvements.
   - Learnings: Logistic Regression may not be the best model for image data. Exploring more complex models like the Random Forest model has yielded better results that generally questions if a further CNN is necessary at all.
   - The set of images is not perfect (e.g. w/o seamount often just grey space), it could be an aim for the CNN to work with more difficult images.

6. **Challenges and Errors**:
   - to find an appropriate baseline model (because this kind of task was not known to us in connection with image recognition before)
   - to interpret the results (Random Forest looks perfect, but is it (or is it maybe just because now it can differentiate between colourful and not colourful images?)
