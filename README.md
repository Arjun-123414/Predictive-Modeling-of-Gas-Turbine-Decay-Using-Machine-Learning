# GT Turbine Decay State Prediction

This project is designed to predict the **GT Turbine decay state coefficient** based on operational parameters of a gas turbine. The machine learning model is built using regression techniques and deployed via a Flask web application. Users can input turbine-related parameters and get predictions through a simple, user-friendly interface.


## Overview

The aim of this project is to predict the **GT Turbine decay state coefficient** based on a variety of input parameters related to the operation of a gas turbine. This prediction is essential for proactive maintenance and optimizing turbine performance.

### Features
- A Flask web app for predicting the GT Turbine decay state.
- **Input fields** for various turbine parameters, including lever position, ship speed, torque, and pressure.
- **Real-time prediction** using a pre-trained Random Forest regression model.
- **Interactive web interface** created using HTML and CSS.

## Folder Structure

```bash
├── Notebook_files/               # Jupyter Notebooks for model training and EDA
│   ├── Model_training.ipynb      # Notebook for model training and evaluation
│   └── eda_of_project.ipynb      # Notebook for Exploratory Data Analysis (EDA)
│
├── notebook/                     
│   ├── Cleaned_data/             # Processed datasets used for training
│   │   └── GasTurbine_Handled.csv# Cleaned gas turbine dataset
│   └── data/                     # Raw datasets for reference
│       └── Conditional_Base_Monitoring...csv # Raw data for conditional base monitoring
│
├── templates/                    # HTML templates for Flask
│   └── index.html                # Main page HTML template
│
├── .gitignore                    # Git ignore file to exclude unnecessary files
├── app.py                        # Flask application code
├── rf.pkl                        # Serialized (Pickle) Random Forest model
├── requirements.txt              # List of Python dependencies
├── setup.py                      # Script for setting up the environment
└── README.md                     # Project documentation
