# Camera Viewer Application

This Python application uses OpenCV and PyQt5 to display video streams from two cameras in a graphical user interface (GUI).

---

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Code Explanation](#code-explanation)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Description

The application captures video streams from two cameras (specified by RTSP URLs), processes the frames in separate threads, and displays the live video feeds side by side in a GUI window.

---

## Features
- **Multithreaded Video Capture**: Efficiently captures frames from multiple cameras using separate threads.
- **Real-Time Display**: Shows live video feeds from two cameras simultaneously.
- **PyQt5 GUI**: Utilizes PyQt5 for a responsive and customizable graphical user interface.
- **Graceful Exit**: Closes the application smoothly when the `Q` key is pressed.

---

## Prerequisites

- Python 3.x
- OpenCV (`opencv-python`)
- PyQt5

---

## Installation

### Clone or Download the Repository
Clone the repository or download the script to your local machine.

### Install Required Packages
Install the necessary Python packages using pip:
```bash
pip install opencv-python PyQt5
```

Alternatively, use the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

**`requirements.txt` content:**
```
opencv-python
PyQt5
```

---

## Usage

### Update RTSP URLs
Replace the RTSP URLs in the script with your camera stream URLs:
```python
thread1 = ThreadedCamera("rtsp://your_camera_ip:port/stream1", frame_queue1)
thread2 = ThreadedCamera("rtsp://your_camera_ip:port/stream2", frame_queue2)
```

### Run the Script
Execute the script using Python:
```bash
python your_script_name.py
```

### View the Streams
- A GUI window titled **"Camera View"** will open.
- Live video feeds from the two cameras will be displayed side by side.

### Exit the Application
Press the `Q` key to close the application gracefully.

---

## Configuration

### Adjust Queue Size
The queues for frame storage have a maximum size of 10. You can modify this if needed:
```python
frame_queue1 = queue.Queue(10)
```

### Modify Display Size
To change the display size of the video feeds, adjust the scaling in the `display_image` method:
```python
p = convert_to_Qt_format.scaled(width, height, QtCore.Qt.KeepAspectRatio)
```

---

## Code Explanation

### 1. ThreadedCamera Class
- **Purpose**: Captures video frames from a camera stream in a separate thread.
- **Key Methods**:
  - `__init__`: Initializes the thread with the camera ID and frame queue.
  - `run`: Continuously reads frames from the camera and places them into the queue.

### 2. App Class
- **Purpose**: Creates the GUI window and displays the video feeds.
- **Key Methods**:
  - `__init__`: Initializes the GUI components.
  - `init_ui`: Sets up the layout, labels, and timers for updating images.
  - `update_image1` & `update_image2`: Retrieve frames from the queues and display them.
  - `display_image`: Converts OpenCV images to Qt format and updates the labels.
  - `keyPressEvent`: Handles key press events to close the application.

### 3. Main Execution Block
- Creates **Frame Queues**: For thread-safe communication between capture threads and the GUI.
- Initializes the **GUI Application**: Sets up the PyQt5 application and displays the window.
- Starts **Camera Threads**: Begins capturing video from the specified RTSP URLs.
- Runs the **Event Loop**: Keeps the application running until exited.

---

## Troubleshooting

### Video Stream Not Displaying
- Ensure the RTSP URLs are correct and accessible.
- Check network connectivity to the camera streams.

### ModuleNotFoundError
- Verify that all required packages are installed.
- Use the pip install commands provided in the Installation section.

### Application Freezes or Crashes
- Reduce the frame queue size if memory consumption is high.
- Ensure your system meets the hardware requirements for video processing.

### PyQt5 Compatibility Issues
- Make sure PyQt5 is compatible with your Python version.
- Consider creating a virtual environment to manage dependencies.

---

## License

This project is open-source and available under the [MIT License](LICENSE).
