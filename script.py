import cv2
import numpy as np


def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x, y)
        cv2.line(window, (x, y), (x + 1, y + 1), (redIntensity, greenIntensity, blueIntensity), 5)
        print(blueIntensity)


def nothing(x):
    pass


# Creating the window and trackbars
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

cv2.createTrackbar('Red\nChannel', 'image', 0, 255, nothing)
cv2.createTrackbar('Blue\nChannel', 'image', 0, 255, nothing)
cv2.createTrackbar('Green\nChannel', 'image', 0, 255, nothing)

while True:
    redIntensity = cv2.getTrackbarPos('Red\nChannel', 'image')
    blueIntensity = cv2.getTrackbarPos('Blue\nChannel', 'image')
    greenIntensity = cv2.getTrackbarPos('Green\nChannel', 'image')

    # Initialising a black background of the resolution 512x512
    window = np.zeros((512, 512, 3), dtype=np.uint8)

    # Initialising a color viewer of the resolution 200x200
    colorViewer = np.zeros((200, 200, 3), dtype=np.uint8)

    # Setting the colorviewer's color on the basis of the values in the trackbars
    colorViewer[np.where((colorViewer == [0, 0, 0]).all(axis=2))] = [blueIntensity, greenIntensity, redIntensity]

    # Adding the color viewer to the top left of the main background
    window[0:200, 0:200] = colorViewer[0:200, 0:200]

    # Setting a white border of 5px width around the color viewer
    window[0:5, 0:200] = [255, 255, 255]
    window[195:200, 0:200] = [255, 255, 255]
    window[0:200, 195:200] = [255, 255, 255]
    window[0:200, 0:5] = [255, 255, 255]

    # Adding the text to the right of the color viewer
    cv2.putText(window, " <= The color you chose", (225, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 1)

    # Displaying the main window
    cv2.imshow('image', window)

    # Press Esc to break the while loop (Move on to close the window)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
