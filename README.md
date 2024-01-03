# Scientific Project Repository
## Notes
- Please make sure to install **Requirements.txt**
- The code was run on **Google colab**

## Data
- Raw data in XML format inside semeval14 folder
- Data folder contains processed DataFrame as train_df and test_df
- Processed dataframes inclueds cleaned text, multibinarized labels and joint labels as well
- TF-IDF vectorizer is also saved as joblib file along with vectorized train and test text

## Notebooks
- **01_data_processing.ipynb** : Basic data processing and cleaning
- **02_SVM_boosting.ipynb** : SVM and Gradient boosting models
- **03_LSTM.ipynb** : LSTM model implementation and training
- **04_BERT.ipynb** : BERT implementation with tokenizer and training
