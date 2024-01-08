# Advanced Cloud Project

This repository contains code for training a machine learning model and deploying it as a web service using AWS Lambda and API Gateway.

## Directory Structure

- /model_training_code
    - train_model.py: Contains code for training the machine learning model.
    - requirements.txt: Lists the Python libraries and dependencies needed for the code to run.
    - /data
        - dataset.csv: The dataset used for training the model.
- /model_deployment_code
    - app.py: Contains code to deploy the trained model as an API for inference.
    - requirements.txt: Lists the Python libraries and dependencies needed for the code to run.
- README.md: This file.
- /deployment_scripts
    - deploy_model.sh: Script to deploy the trained model to AWS Lambda or API Gateway.

## Usage

1. Train the model by running `python train_model.py`.
2. Deploy the model by running `bash deploy_model.sh`.

## License

This project is licensed under the terms of the MIT license.
