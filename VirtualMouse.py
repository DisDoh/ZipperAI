import cv2
import mediapipe as mp
import tkinter as tk
import math
import pyautogui


# Function to map hand landmarks to screen coordinates
def map_landmarks_to_screen_coords(landmark, screen_width, screen_height):
    x = int(landmark.x * screen_width)
    y = int(landmark.y * screen_height)
    return x, y


# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

clicking = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get index finger landmark (assuming right hand for simplicity)
            index_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            middle_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Map hand landmarks to screen coordinates
            index_x, index_y = map_landmarks_to_screen_coords(index_finger_landmark, screen_width, screen_height)
            thumb_x, thumb_y = map_landmarks_to_screen_coords(thumb_finger_landmark, screen_width, screen_height)
            middle_x, middle_y = map_landmarks_to_screen_coords(middle_finger_landmark, screen_width, screen_height)

            # Calculate distance between thumb and middle finger tips
            distance = calculate_distance((thumb_x, thumb_y), (middle_x, middle_y))

            # Check if distance is small enough to simulate click
            if distance < 50:
                if not clicking:
                    pyautogui.mouseDown()
                    clicking = True
            else:
                if clicking:
                    pyautogui.mouseUp()
                    clicking = False

            pyautogui.moveTo(index_x, index_y)

    cv2.imshow('Virtual Mouse', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
