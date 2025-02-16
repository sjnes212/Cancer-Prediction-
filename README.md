Breast Cancer Prediction Project

Overview
This project aims to develop a machine learning model to predict whether a patient has breast cancer or not based on various features extracted from tumor samples.
Project Structure
The project is organized as follows:

notebooks: Jupyter notebooks used for data exploration and model development.
src: Python scripts for data preprocessing and model training.
app: Flask web application for cancer prediction.
data: Raw dataset (Cancer.csv) used for the project.
models: Saved machine learning models and preprocessors.

Models Trained
The following models were trained and evaluated on the breast cancer dataset:

Logistic Regression
Decision Tree
Random Forest
AdaBoost
Support Vector Machine (SVC)
Naive Bayes
K-Nearest Neighbors

Usage
1. Install the required dependencies:
- pip install -r requirements.txt

2. Run the data preprocessing and model training scripts:
- python src/data_preprocessing.py
- python src/model_training.py

3. Start the Flask web application:
- python app/main.py

Access the web application at http://localhost:5000.

****EXAMPLES****

****Cancer Detected (Malignant)****

![Screenshot (42)](https://github.com/user-attachments/assets/74d1e5ed-d3d3-417c-b6e7-a3c932fe82a2)

****No Cancer (Benign)****

![Screenshot (43)](https://github.com/user-attachments/assets/7a694e08-ea23-4b72-816d-bfc4f836fa02)
