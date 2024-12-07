# Baseline Model

**[Notebook](baseline_model.ipynb)**

1. **Introduction and data choice**: First trials of a base model were done before we settled on a final way of preparing the data. Several possibilities were regarded:
   - using only hand-selected examples of positive/negative examples (e.g. from a certain area)
   - using a lot of automatically downloaded images according to a seamount database worldwide.
   - using only high-resolution bathymetric data or also low.
While high resolution data was preferred, it only existed as asymmetric, diagonal strips of imagery across an otherwise empty or low-resolutioned picture. We settled for high-res data with the low-res "background" parts still in place, as it was easy to generate and seemed quite fluent in the image data (avoiding too much contrast, which has no meaning in the sense of the project).

4. **Baseline Model**: While first trials were actually made with a simple CNN, we settled for a simple logistic regression and, as an alternative, for a random forest model to serve as our baseline approach.# Baseline Model

**[Notebook](baseline_model.ipynb)**

1. **Introduction and data choice**: First trials of a base model were done before we settled on a final way of preparing the data. Several possibilities were regarded:
   - using only hand-selected examples of positive/negative examples (e.g. from a certain area)
   - using a lot of automatically downloaded images according to a seamount database worldwide.
   - using only high-resolution bathymetric data or also low.
While high resolution data was preferred, it only existed as asymmetric, diagonal strips of imagery across an otherwise empty or low-resolutioned picture. We settled for high-res data with the low-res "background" parts still in place, as it was easy to generate and seemed quite fluent in the image data (avoiding too much contrast, which has no meaning in the sense of the project).

4. **Baseline Model**: While first trials were actually made with a simple CNN, we settled for a simple logistic regression and, as an alternative, for a random forest model to serve as our baseline approach.

5. **Model Definition and Evaluation**: (Discuss the models you've implemented, the feature engineering steps you've taken, and how you evaluated their performance. Include a screenshot of the code you used to implement the model.)

6. **Results/Learnings for the rest of the project**: (Present the results in a clear and easy-to-understand format. Use tables, charts, or any other visual aids that you find appropriate.)

7. **Challenges and Errors**:
   - to find an appropriate baseline model (because this kind of task was not known to us in connection with image recognition before)
   - 

5. **Model Definition and Evaluation**: (Discuss the models you've implemented, the feature engineering steps you've taken, and how you evaluated their performance. Include a screenshot of the code you used to implement the model.)

6. **Results**: (Present the results in a clear and easy-to-understand format. Use tables, charts, or any other visual aids that you find appropriate.)

7. **Challenges and Errors**:
   - to find an appropriate baseline model (because this kind of task was not known to us in connection with image recognition before)
   - 
