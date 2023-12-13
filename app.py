import streamlit as st
import cv2
import mediapipe as mp
import numpy as np

def main():
    st.title("Hand Tracking Paint App")

    # Load the drawing tool image
    drawing_tool_image = cv2.imread("drawing.png")
    drawing_tool_image = drawing_tool_image.astype('uint8')

    # Create a canvas
    canvas = st.empty()
    canvas_width, canvas_height = 640, 480
    canvas_image = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    # Initialize hand tracking
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    # Tool selection variables
    tool_names = ["circle", "line", "rectangle", "erase"]
    current_tool = "circle"
    tool_radius = 10

    while True:
        # Get webcam frame
        _, frame = st.beta_read_all()

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and get hand landmarks
        results = hands.process(rgb_frame)

        # Draw hand landmarks on the canvas
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * canvas_width), int(landmark.y * canvas_height)
                    cv2.circle(canvas_image, (x, y), tool_radius, (255, 0, 0), -1)

                    # Check if a tool is selected based on hand position
                    if x < 50 and y < 50:
                        current_tool = "circle"
                    elif x < 100 and y < 100:
                        current_tool = "line"
                    elif x < 150 and y < 150:
                        current_tool = "rectangle"
                    elif x < 200 and y < 200:
                        current_tool = "erase"

        # Display the drawing tool image on the canvas
        canvas_image[:drawing_tool_image.shape[0], :drawing_tool_image.shape[1]] = drawing_tool_image

        # Display the canvas image
        canvas.image(canvas_image, channels="BGR", use_column_width=True)

        # Display current tool name
        st.text(f"Current Tool: {current_tool}")

if __name__ == "__main__":
    main()
