
# Body Tracking module

This project implements a body tracking module using Mediapipe, a powerful library for various computer vision tasks. The module can track and analyze human body movements and gestures in real-time video streams or pre-recorded videos. It leverages the robustness and accuracy of Mediapipe's pre-trained models to detect key points on the human body, such as joints and landmarks, enabling a wide range of applications in fitness tracking, motion analysis, and human-computer interaction.
## Features

- Real-time Body Tracking: The module provides real-time tracking of human body movements, allowing for live analysis of gestures and postures.
- Robustness and Accuracy : The hand tracking model achieves high accuracy and robustness across various lighting conditions, hand poses, and backgrounds.
- Easy Integration : The module is designed to be easily integrated into existing Python projects, providing a simple API for accessing hand tracking functionality.
- Customization : Users can customize the module to suit their specific requirements, such as adjusting tracking parameters, defining custom gestures, or integrating with other computer vision algorithms.
- Visualization: The module includes visualization tools for displaying tracked body keypoints and skeletons, facilitating debugging and analysis.
## Requirements

- Python
- Mediapipe
- Numpy
- OpenCV


## Installation

- Clone this repository to your local machine.
- Install the required dependencies using pip install -r requirements.txt.
- Optionally, download additional MediaPipe models or assets if required for specific functionality.
    
## Usage

- Import the BodyTrackingModule class from the module.
- Create an instance of the BodyTrackingModule.
- Initialize the hand tracking module.
- Provide webcam or video input to the module for real-time Body tracking.
- Access detected hand landmarks and perform gesture recognition as needed.
- Integrate the module with your application logic to enable interactive hand tracking features.
## Screenshots

![Video used for Prediction](https://drive.google.com/file/d/1FjgYKJEZUxG1ClmtOLg5b6xCuVx5mpQt/view?usp=drive_link)

![Output](https://drive.google.com/file/d/1otKOEqF46lGDkhD_wT8gOmV-iy6mZa29/view?usp=drive_link)

