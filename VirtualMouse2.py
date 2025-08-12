import cv2
import numpy as np
import time
import pyautogui
import HandTrackingModule as htm

# Camera settings
wCam, hCam = 640, 480
frameR = 100  # Reduce edge area where hand movements will be considered
smoothening = 7  # Increased smoothing factor for smoother movement

# Initialize variables
pTime = 0
plocX, plocY = 0, 0  # Previous location of the cursor
clocX, clocY = 0, 0  # Current location of the cursor
singleClickPerformed = False  # To track if a single click has already been performed

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Using DSHOW for better webcam performance on Windows
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.HandDetector(maxHands=1)  # Detecting only one hand for simplicity

# Get screen size
wScr, hScr = pyautogui.size()

while True:
    success, img = cap.read()

    # Find hand landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:  # Check if landmarks are detected
        # Index finger tip position
        x1, y1 = lmList[8][1:]

        # Get the positions as relative to the screen size (mapping screen coordinates)
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

        # Smooth the movement with more control
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        # Move the mouse
        pyautogui.moveTo(wScr - clocX, clocY)

        plocX, plocY = clocX, clocY

        # Optional: Drawing a circle to indicate finger position
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

        # Detect clicks based on finger configuration
        fingers = detector.fingersUp()

        # Single left-click: Index and middle fingers up
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:
                if not singleClickPerformed:  # Only perform click if it hasn't been performed already
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    pyautogui.click()
                    singleClickPerformed = True  # Mark click as performed
            else:
                singleClickPerformed = False  # Reset click tracking if fingers are not close

        # Continuous click: Index, middle, and ring fingers up
        elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:
            pyautogui.click()

        # Right-click: Thumb is up
        elif fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0:
            pyautogui.rightClick()

    # Frame rate calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

    # Display the frame
    cv2.imshow("Virtual Mouse", img)
    cv2.waitKey(1)
