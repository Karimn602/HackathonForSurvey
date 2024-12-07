# Logistic Regression Analysis with L2 Regularization and other Models

This repository contains a Jupyter Notebook that demonstrates logistic regression with L2 regularization and other Models , hyperparameter tuning using GridSearchCV, and evaluation on a survey dataset. The project explores factors affecting survey responses and aims to build a robust predictive model.

## Project Objective
The main goals of this project are:
- Preprocess and clean survey data stored in an Excel file.
- Perform logistic regression with L2 regularization and other Models.
- Use GridSearchCV for hyperparameter tuning to optimize the model.
- Handle class imbalance using balanced class weights.
- Evaluate the model’s performance using accuracy, precision, recall, and F1-score.

## Dataset
The dataset is stored in the file:
- **`2024_PersonalityTraits_SurveyData.xls`**

It contains survey responses with various demographic, behavioral, and financial attributes. Key features include:
- Personality traits (e.g., openness, anxiety, dependability).
- Financial impact of the Lebanese economic crisis.
- Social and lifestyle habits.

### Key Columns
- **`financial_impact`**: Target variable indicating the degree of financial impact.
- **Other variables**: Include demographic, lifestyle, and survey responses.

## Files in the Repository
- **`HackathonFinal.ipynb`**: Jupyter Notebook with the following steps:
  1. Data loading and preprocessing.
  2. Feature engineering and scaling.
  3. Logistic regression with L2 regularization and Other Models.
  4. Hyperparameter tuning using GridSearchCV.
  5. Model evaluation and result visualization.


## How to Use
### Prerequisites
Ensure Python is installed, along with `pip`. Install the necessary dependencies using:
pip install -r pandas
numpy
scikit-learn
matplotlib
seaborn
openpyxl


## Results
The analysis identifies the best logistic regression model using L2 regularization. Key results include:

## Hyperparameter tuning results showing optimal C values.
Performance metrics (accuracy, precision, recall, F1-score) indicating model effectiveness.

## Acknowledgments
Special thanks to the contributors of the dataset and the development community for tools and libraries used in this project.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
