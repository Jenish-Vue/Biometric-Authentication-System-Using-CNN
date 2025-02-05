# Fingerprint Authentication System for Lab Access
## Project Overview

This project implements a Fingerprint Authentication System for lab access using Convolutional Neural Networks (CNNs) for binary classification. The system verifies whether the provided fingerprint matches an authorized person's fingerprint or not. If a match is found, the system grants access and identifies the person. This is achieved by training a CNN model using a dataset of fingerprint images, which is then integrated with a backend and frontend.

## Features

    1. Fingerprint Authentication:  
     The system can verify whether a fingerprint is authorized and identify the individual.
    2. Binary Classification: 
      The CNN model classifies the fingerprint images as "same" or "different" for authentication purposes.
   3.  Frontend Interface:
      A simple HTML/CSS frontend is used to capture the fingerprint image, which is then sent to the backend for comparison.
    4. Backend Integration:
      Flask is used for handling backend requests, image processing, and matching the fingerprint against the authorized database.
    5.Identification and Access Control:
       The system identifies the person if the fingerprint matches and grants access accordingly.

## Dataset

     The dataset used for training the model is sourced from https://www.kaggle.com/datasets/ruizgara/socofing
     The dataset consists of fingerprint images of 600 subjects, divided into two folders:

         Real: Contains genuine fingerprint samples.
         Altered: Contains altered (modified) fingerprint samples.

      Each image in the dataset is preprocessed for fitting the CNN model, and the dataset is used to train the system to classify whether the fingerprints are the same or different.

## How It Works

### 1. Data Preprocessing
         The fingerprint images are processed to ensure they are in a suitable format for training. 
         This includes resizing, normalization, and splitting the dataset into training and testing sets.
         
### 2. CNN Model Training

        A Convolutional Neural Network (CNN) is trained to classify whether two fingerprint images are the same or different. The model is designed to learn the distinguishing features of a fingerprint and 
        determine if a match is found.
        
### 3. Backend Integration with Flask

       Once the model is trained, it is integrated into a Flask-based backend. The backend receives the fingerprint image from the frontend, processes it, 
       and compares it to the authorized fingerprints stored in  the database.
       
### 4. Frontend Interaction

          The user interacts with a simple HTML/CSS interface to capture their fingerprint. The image is sent to the Flask backend 
          via an HTTP request for authentication and identification.
          
### 5. Authentication and Identification

        The backend compares the captured fingerprint to those stored in the database. If a match is found, the person is identified, and access is granted. 
        If no match is found, access is denied.

### Conclusion

The Fingerprint Authentication System for Lab Access demonstrates the power of combining deep learning techniques, biometric authentication, and web technologies to create a robust and secure system. By leveraging a Convolutional Neural Network (CNN) for fingerprint classification and integrating it with a Flask backend and a user-friendly frontend, the system effectively identifies authorized individuals and grants access accordingly.
