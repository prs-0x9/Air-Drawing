# Air-Drawing

A computer vision application that allows you to draw in the air using your index finger, tracked through your webcam with MediaPipe's hand detection—created for Northern Illinois University's Huskie Hackers club, February 2025 pizza hack.

## Features

- Real-time hand tracking using MediaPipe
- Draw on a virtual canvas by moving your index finger
- Merge of webcam feed with your drawings
- Clear canvas functionality
- Simple user interface

## Prerequisites

- Python 3.x
- OpenCV (cv2)
- MediaPipe
- NumPy
- Webcam or camera device
- Basic knowledge of Python

## Installation

1. Clone the repository

    ```
    git clone https://github.com/prs-0x9/Air-Drawing.git
    ```

2. Navigate to the project directory

    ```
    cd airdraw
    ```

3. Install the required dependencies

    ```
    pip install opencv-python mediapipe numpy
    ```

## Usage

1. Run the Python script

    ```
    python airdraw.py
    ```

2. Position yourself in front of the webcam
3. Use your index finger to draw in the air
4. Press 'c' to clear the canvas
5. Press 'q' to quit the application

## Controls

- Move your index finger to draw
- Press 'c' to clear the canvas
- Press 'q' to exit the program

## Error Handling

- The application checks if your webcam is properly connected
- Handles failures in frame capture
- Gracefully exits if no webcam is available

## Project Structure

```
airdraw/
│
├── airdraw.py        # Main source code file
├── README.md         # This file
```

## How It Works

1. The webcam captures video feed
2. MediaPipe's hand tracking model detects your hand and its landmarks
3. The application tracks the position of your index finger (landmark 8)
4. As you move your finger, lines are drawn on a virtual canvas
5. The canvas is merged with the webcam feed for display

## Future Improvements

- Multiple color options
- Adjustable line thickness
- Different drawing tools (circle, rectangle, etc.)
- Save drawings as images
- Eraser functionality
- Multi-hand support for collaborative drawing
- Gesture-based commands
- Undo/redo functionality
- Cloud version two allow a shared virtual canvas

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Paris Richards

## Acknowledgments

- MediaPipe team for the hand tracking solution
- OpenCV community

## Contact

- GitHub: [@prs-0x9](https://github.com/prs-0x9)
- LinkedIn: [Paris Richards](https://www.linkedin.com/in/parisrichards974/)