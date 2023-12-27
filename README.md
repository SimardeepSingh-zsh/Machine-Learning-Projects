# Image Captioning using CNN and RNN

This repository contains scripts for image captioning using convolutional neural networks (CNN) and recurrent neural networks (RNN).

## Project Structure
- `data/`: Directory for storing the dataset used for training.
- `models/`: Directory to store trained model weights and configurations.
- `src/`: Contains Python scripts for preprocessing, model architecture, training, evaluation, and prediction.
- `preprocess.py`: Script for data preprocessing.
- `model.py`: Contains the model architecture for image captioning.
- `train.py`: Script for training the image captioning model.
- `evaluate.py`: Script for evaluating the trained model.
- `predict.py`: Script for generating captions for new images.
- `README.md`: Information about the project and instructions to run the scripts.

## How to Run
1. Download the COCO dataset and place it in the `data/` directory.
2. Run `preprocess.py` to preprocess the data.
3. Run `train.py` to train the model.
4. Run `evaluate.py` to evaluate the trained model.
5. Use `predict.py` to generate captions for new images.

## Requirements
- Python 3.x
- TensorFlow
- Other necessary libraries as mentioned in the scripts.
