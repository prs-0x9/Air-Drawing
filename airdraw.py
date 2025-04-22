import cv2
import mediapipe as mp
import numpy as np

# Access the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")

# Set the width and height of the webcam feed (640x480)
cap.set(3, 640) # 3 is the width
cap.set(4, 480) # 4 is the height

# Load the MediaPipe hand model
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Create a blank canvas
canvas = np.zeros((480, 640, 3), dtype=np.uint8)
# Store prevoius finger position
prev_x, prev_y = None, None

# Capture the webcam feed
while cap.isOpened():
    success, frame = cap.read() # Read the frame
    if not success:
        print("Failed to capture a frame!")
        break
    if success:
        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)
        # Convert the BGR image to RGB
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Process the frame
        result = hand.process(RGB_frame)
        # Merge the frame with the original frame
        merged_frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    if result.multi_hand_landmarks:
        # Loop through each detected hand
        for hand_landmarks in result.multi_hand_landmarks:
            # Get the index finger tip coordinates (Landmark 8)
            index_finger_tip = hand_landmarks.landmark[8]
            h, w, _ = frame.shape
            x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            if prev_x is not None and prev_y is not None:
                # Draw a line from the previous position to the current position
                cv2.line(canvas, (prev_x, prev_y), (x, y), (255, 0, 0), 5)
            prev_x, prev_y = x, y  # Update previous position
            #print(hand_landmarks)
            # Draw the hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Merge the drawn frame with the canvas
            merged_frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)
    cv2.imshow('Webcam Feed', merged_frame) # Display the frame
    key = cv2.waitKey(1) & 0xFF 
    if key == ord('c'): # Check for user input (c to clear the canvas)
     canvas = np.zeros((480, 640, 3), dtype=np.uint8) # Clear the canvas   
    elif key == ord('q'): # Check for user input (q to quit)
        break

cap.release() # Release the webcam
cv2.destroyAllWindows() # Close the window
hand.close() # Close the MediaPipe hand model