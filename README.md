# Project Title

Deep Learning-Based Phishing Detection: A Dual Approach Using CNN and CNN-LSTM


## Overview
This project focuses on detecting phishing websites using a deep learning approach. Specifically, we employ Convolutional Neural Networks (CNN) and a hybrid CNN-Long Short-Term Memory (CNN-LSTM) model to enhance detection accuracy and robustness.


## Models Used

### Dataset

This model is trained and validated using the **Phishing Websites Features** dataset. This dataset provides a comprehensive set of features that are critical for distinguishing phishing websites from legitimate ones.


### AI Model

This project utilizes the **Phishing Website Detection CNN-LSTM** model as the core component of our architecture. This model is specifically designed for phishing detection and takes advantage of CNN and LSTM networks.


### References
- Mohammad, Rami M., Fadi Thabtah, and Lee McCluskey. "Phishing websites features." School of Computing and Engineering, University of Huddersfield (2015).
- pr4nav_101, “Phishing Website Detection CNN-LSTM”: Available: https://www.kaggle.com/code/pr4nav101/phishing-website-detection-cnn-lstm.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [Documentation](#documentation)
- [Acknowledgments](#acknowledgments)


## Installation

To run the project on your local machine, follow these steps:


### Prerequisites

Install the Anaconda3


#### Gernate the dataset

- Visual Studio Code
- Python 3.11.8
- BeautifulSoup


#### Training and Testing Model

- Anaconda3
- Python 3.7
- Keras
- Tensorflow
- Jupyter


### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/WSimonHo/smart-website-scanner/tree/master
    ```
2. Navigate to the project directory:
    ```sh
    cd ./smart-website-scanner
    ```
3. Create a virtual environment:
    ```sh
    conda create --name ai_model python=3.7
    ```
4. Start the anaconda virtual environment:
    ```sh
    conda activate ai_model
    ```
5. Install Tensorflow:
    ```sh
    conda install tensorflow
    ```
6. Install Keras:
    ```sh
    conda install -c conda-forge keras
    ```
7. Install Jupyter Notebook:
    ```sh
    conda install jupyter notebook
    ```


## Usage


### Dataset Generate

To generate the dataset for phishing detection, you can follow the example script provided in the `model` directory. Below is a basic usage example:

#### Genrate the Phishing Websites URL Features Dataset

1. Open the `` in VSCode
2. Insert the csv file that for generate the Phishing Websites URL Features
3. Change the name of the data set that will be generated
4. Run the script and will see the dataset generated


#### Genrate the Phishing Websites Content Features Dataset

1. Open the `` in VSCode
2. Insert the csv file that for generate the Phishing Websites URL Features
3. Change the name of the data set that will be generated
4. Run the script and will see the dataset generated


#### Merge Legitimate dataset and Phishing dataset into one Dataset

1. Open the `` in VSCode
2. Change the datasets name
3. Change the name of the data set that will be generated
4. Run the script and will see the dataset generated


### AI Model

To use the AI model for phishing detection, you can follow the example script provided in the `model` directory. Below is a basic usage example:

1. Run the Anaconda
2. Change the virtual environment to ai_model
1. Start the Jupyter Notebook
2. Update the dataset that for generate the Phishing Websites URL Features
3. Run the script


## Testing

The



## Features

- Dual Approach: Implementation of both CNN and CNN-LSTM models to leverage their respective strengths in phishing detection.
- Enhanced Accuracy: Aiming to improve detection accuracy through the combination of convolutional and sequential learning techniques.
- Robustness: Developing a more robust detection system capable of identifying various phishing tactics.
- Scalability: Ensuring the models can handle large datasets and adapt to new phishing strategies over time.
- Comparative Analysis: Providing a detailed comparison between the performance of CNN and CNN-LSTM models in phishing detection.


## Documentation


## Acknowledgments

This README.md structure clearly mentions the use of both the model and the dataset, provides references to their sources, and includes essential information for users to understand and utilize your project.
