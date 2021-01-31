# Galactic Search Path Classifier Jupyter Notebook

Training Notebook and Dataset for Galactic Search Path Determination Model 2021

Keras neural network to determine path configuration for 2021 FRC Galactic Search Challenge

Model trained here to be deployed to rPi running [mcqueen-vision](https://github.com/frc-862/mcqueen-vision)

## Project Structure

- `/input/` | the images to be used during the training process
  - `A-BLUE` | Path A, Blue Layout Images
  - `A-RED` | Path A, Red Layout Images
  - `B-BLUE` | Path B, Blue Layout Images
  - `B-RED` | Path B, Red Layout Images
- `model-training.ipynb` | Jupyter Notebook to train Keras network
- `convert.ipynb` | Jupyter Notebook to convert Keras network to TensorFlow format so it can be used by [OpenCv Dnn](https://docs.opencv.org/3.4/javadoc/org/opencv/dnn/Dnn.html)
- `final-classifier.h5` | Keras model
- `final-classifier.pb` | TensorFlow model to be deployed to pi
