# Real-Time Color Detection

## Overview
This script performs real-time color detection using OpenCV. It identifies a specified color in a video stream from the webcam, highlights the detected area, and displays it in a live feed.

## Features
- Captures video feed from the webcam.
- Detects a specified color (default: yellow) in real time.
- Highlights the detected area with a bounding box.
- Displays the live video feed with the detected region marked.

## Libraries Used
- `os`: For file and directory operations.
- `cv2` (OpenCV): For video capture, color conversion, and real-time visualization.
- `PIL` (Pillow): For image manipulation.
- `util`: Custom module containing the `get_limits` function to determine HSV limits for a specified color.

## How to Run
1. **Install Dependencies**:
   Ensure you have Python installed. Use the following command to install the required libraries:
   ```bash
   pip install opencv-python pillow
   ```

2. **Prepare the Environment**:
   Ensure the `util.py` file is in the same directory as this script, with the `get_limits` function implemented.

3. **Run the Script**:
   Execute the script using the following command:
   ```bash
   python main.py
   ```

4. **Interact with the Feed**:
   - The script will open a live video feed from your webcam.
   - Press the `q` key to exit the application.

## Customization
- **Change the Target Color**:
  Modify the `yellow` variable to the desired color in BGR format. For example:
  ```python
  yellow = [0, 0, 255]  # Red color in BGR
  ```
- **Adjust the `get_limits` Function**:
  Ensure the `get_limits` function in `util.py` provides accurate HSV ranges for the chosen color.

## Notes
- Ensure your webcam is properly connected and accessible.
- The `get_limits` function is essential for the script to work. It should return `lower_limit` and `upper_limit` values for the HSV range of the target color.
- The script is set to detect yellow by default. Modify the `yellow` variable for other colors.

## Acknowledgments
This project leverages OpenCV and Pillow for efficient color detection and visualization in real time.

