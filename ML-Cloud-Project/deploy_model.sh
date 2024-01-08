#!/bin/bash

# Package your code and dependencies
zip deployment_package.zip app.py model.joblib

# Deploy your model/application using AWS CLI
aws lambda create-function --function-name my_model --runtime python3.8 --role my_lambda_role --handler app.predict --zip-file fileb://deployment_package.zip
