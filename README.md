# Image-Augmentation

## Description

Performs the following image augmentations:

1. varying hue
2. grayscaling
3. flipping
4. varying brightness
5. varying contrast

This repository randomly augments images that have been sorted according to the Default Directory Organisation

## Default Directory Organisation:

- Training Data
  - Class 1
    - Augmented Images
    - originalImage1.jpg
    - originalImage2.jpg
    - ...
  - Class 2
    - Augmented Images
    - originalImage1.jpg
    - originalImage2.jpg
  - ...

This can be adjusted according to the use case and existing system used from image_augmentation.py

## Required dependencies:

1. pip install numpy
2. pip install opencv-python