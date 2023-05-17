# Rental_Bike_share_prediction
## Project Objective
The objective of this project is to create a solution for user which can help them to predict demand for rental bikes for Capital Bikes in Washington DC so that they can strategically fullfill demand.

## Tools Used
- Jupyter Notebook
- VS Code
- Flask
- Database : MongoDB
- Machine Learning Algorithms: Random Forest and XG Boost
- MLOps
- HTML


## Dataset
We have taken data from 2018 to January 2022 for training, Feb 2022 to Mar 2022 for Testing.

Ride was collected from Capital Bike Share website.
link: http://capitalbikeshare.com/system-data

Weather Data was collected from link: http://www.freemeteo.com

We have derived the final dataset for model training from above two datasets.

## Installation

Install my-project with npm

### Step 1 - Clone the repository
```bash
git clone https://github.com/sumeet0701/shipment-cost-prediction.git
```

### Step 2 - Create a conda environment after opening the repository

```bash
conda create -n env_name python
```

```bash
conda activate env_name
```

### Step 3 - Install the requirements
```bash
pip3 install -r requirements.txt
```


### Step 4 - Train Model
```bash
python demo.py

```

### Step g - Run the Prediction application server [Using Flask API]
```bash
python main.py
```

### Step 7 - Prediction application [Using Flask API]
```bash
http://localhost:5000

```

## Project Details
There are six packages in the pipeline: Config, Entity, Constant, Exception, Logger, Components and Pipeline

### Config
This package will create all folder structures and provide inputs to the each of the components.

### Entity
This package will defines named tuple for each of the components config and artifacts it generates.

### Constant
This package will contain all predefined constants which can be used accessed from anywhere

### Exception
This package contains the custom exception class for the Prediction Appliaction

### Logger
This package helps in logging all the activity

# Components
--------
## Data Ingestion 
-----
### Folder structure 

![Before](https://user-images.githubusercontent.com/109200332/226115648-39a3c045-c68f-4a44-8398-2d643aa9fec9.png)


#### Data Ingestion 
This module downloads the data from the link, unzip it, then stores entire data into Db.
From DB it extracts all data into single csv file and split it into training and testing datasets.

![Data_Ingestion](https://user-images.githubusercontent.com/109200332/226117526-e5669825-d7e4-4e9a-8347-8ce11d314386.png)


## Data Validation

Data Validation: This module validates whether data files passed are as per defined schema which was agreed upon by client.


![Data_Validation](https://user-images.githubusercontent.com/109200332/226121268-9ef2e4ca-21d1-4f9b-a6f5-cd8c15323bc4.png)


## Data Transformation

This module applies all the Feature Engineering and preprocessing to the data we need to 
train our model and save  the pickle object for same.

![Data Transformation](https://user-images.githubusercontent.com/109200332/226129709-116764b4-8eab-43e8-bacb-934ad7f2ad2a.png)

## Model Trainer
 This module trains the model on transformed data, evalutes it based on R2 accuracy score and 
 saves the best performing model object for prediction

![Model Trainer](https://user-images.githubusercontent.com/109200332/226136355-3704614b-c6e6-4eb7-b39c-e29ce9127847.png)

### Pipeline
This package contains two modules:
1. Training Pipeline: This module will initiate the training pipeline where each of the above mentioned components  
                      will be called sequentially untill model is saved.
2. Prediction Pipeline: This module will help getting prediction from saved trained model.


## Project Archietecture

![Customer Personality Analysis (1)](https://github.com/sumeet0701/shipment-cost-prediction/assets/63961794/96191954-0dd7-4d87-b233-b8f5acaef742)

## Development Archietecture
![deploment](https://github.com/sumeet0701/shipment-cost-prediction/assets/63961794/cc656631-3588-468d-9dc9-17d0bcd11843)

 



## 🔗 Links
[![Github](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/sumeet0701/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sumeet-maheshwari/)





## Authors

- [@Maheshwari Sumeet](https://github.com/sumeet0701)




