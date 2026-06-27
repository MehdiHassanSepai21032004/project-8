OpenCV Image and Video Processing Basics:-

This repository contains a comprehensive Python script demonstrating fundamental image and video processing techniques using OpenCV (`cv2`) and NumPy. 
Features:-

The script is organized into modular functions, each demonstrating a specific computer vision operation:
Image Processing :-
* Basic I/O & Manipulation:** Reading, resizing, displaying, and saving images.
* Morphological Operations:** Erosion, Dilation, Opening, Closing, Tophat, Blackhat, and Morphological Gradient.
* Geometric Transformations:** * Flipping (Horizontal, Vertical, Both)
  * Resizing (by percentage scale)
  * Shifting (Translation via `warpAffine`)
  * Rotation (`getRotationMatrix2D`)
* Drawing & Annotation:** Overlaying shapes (lines, rectangles, circles, polygons) and text onto images.
* Filtering & Smoothing:** Gaussian Blur, Median Blur, and Bilateral Filtering.
* Thresholding & Edge Detection:** Binary thresholding and Canny Edge Detection.

Video Processing :-
* Video Playback:** Reading and displaying frames from an `.mp4` file.
* Video Writing:** Capturing video, processing frames, and saving the output to a new `.mp4` file using the `mp4v` codec.
* Live Feed:** Accessing the computer's webcam for real-time video capture and display.

Prerequisites :-

Ensure you have Python installed on your system. You will also need to install the required libraries:
