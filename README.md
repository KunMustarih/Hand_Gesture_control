# Hand_Gesture_control
This GitHub project enables users to control media playback and presentation slides using hand gestures. It leverages Python and several libraries, including cv2, Mediapipe, pyautogui, and win32gui, to detect hand gestures and trigger actions accordingly. The project provides an accessible and interactive way to enhance the viewing experience and accessibility of media content.

Table of Contents
Abstract
Introduction
Libraries
Project Structure
Usage
Conclusion
References
Abstract
This project explores the use of hand gestures for controlling media playback and presentation slides. It utilizes Python, cv2, Mediapipe, pyautogui, and win32gui libraries to detect and interpret hand gestures. The resulting program allows users to customize hand gestures for various applications, providing a more interactive and accessible user experience.

Introduction
Computer programming has paved the way for technological advancements that simplify the lives of millions of people. This project focuses on computer automation, specifically using hand gestures to interact with media and presentation software. Real-time hand gesture recognition can significantly enhance user experiences and accessibility across various technology platforms.

The project's motivation stems from the desire to make technology more accessible to users. Google's MediaPipe software plays a crucial role in simplifying hand detection, making it easier to integrate with other APIs like pyautogui and OpenCV. This integration allows users to control media content using hand gestures.

Libraries
MediaPipe
MediaPipe by Google is used for hand and finger tracking. It identifies 21 3D landmarks on the user's hands in a single frame, making real-time performance achievable without requiring a powerful computer. The software includes models for palm detection and hand landmark prediction, contributing to the overall accuracy of hand tracking.

PyAutoGui
PyAutoGui is an API that allows Python scripts to automate mouse and keyboard interactions with other applications. Key features include mouse dragging, button clicking, keypress simulation, and window management (e.g., moving, resizing, maximizing, minimizing, and closing).

OpenCV
OpenCV is an open-source computer vision, machine learning, and image processing library supported by various programming languages, including Python. It enables image and video processing for tasks like facial recognition, object detection, license plate reading, and more. OpenCV can be seamlessly integrated with other libraries and models, such as MediaPipe.

Project Structure
HandTrackingModule.py
This module is responsible for hand detection and landmark tracking. It utilizes cv2 and Mediapipe libraries to capture frames from the camera and detect hand landmarks. Key functions include:

findHands: Converts captured images into RGB format and detects hand landmarks.
findPosition: Returns a list containing the ID numbers and X-Y coordinates of hand landmarks.
fingersUp: Determines which fingers are up and which are down.
Video_Gestured.py
This script imports cv2, HandTrackingModule, and pyautogui libraries. It is designed to work with the VLC media player and control media playback using hand gestures. Key functionalities include:

Playing and pausing the video.
Adjusting volume.
Moving forward and backward in the video.
Exiting the program using the 'Q' key.
Presentation_control.py
This script imports pyautogui, win32gui, and HandTrackingModule. It works with Microsoft PowerPoint to control presentation slides using hand gestures. Gestures include:

Going to the next slide (left-hand thumb up).
Going to the previous slide (left-hand pinky finger up).
Usage
To use this project, follow these steps:

Install the required libraries: cv2, Mediapipe, pyautogui, and win32gui.
Run Video_Gestured.py to control media playback or Presentation_control.py to control PowerPoint presentations.
Follow the specified hand gestures to trigger actions.
Conclusion
This project enhances the user experience and accessibility of media playback and presentations by incorporating hand gestures for control. It showcases the potential of real-time hand gesture recognition in computer automation and offers customizable gestures for various applications.

