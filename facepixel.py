import cv2
import numpy as np

def pixelate_image(image, pixel_size):
    """Pixelate the image by resizing and then resizing back."""
    height, width = image.shape[:2]
    # Resize down to the pixelated size
    small = cv2.resize(image, (width // pixel_size, height // pixel_size), interpolation=cv2.INTER_LINEAR)
    # Resize back to original size
    pixelated = cv2.resize(small, (width, height), interpolation=cv2.INTER_NEAREST)
    return pixelated

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set the desired resolution (e.g., 1920x1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Set the frame rate to 60 FPS
cap.set(cv2.CAP_PROP_FPS, 60)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Flip the frame horizontally to create a mirror effect
    mirrored_frame = cv2.flip(frame, 1)
    
    # Convert to grayscale
    gray_frame = cv2.cvtColor(mirrored_frame, cv2.COLOR_BGR2GRAY)

    # Pixelate the grayscale frame with a smaller pixel size for more detail
    pixelated_frame = pixelate_image(gray_frame, pixel_size=3)  # Smaller pixel size for better detail
    
    # Invert the colors so black becomes white and white becomes black
    inverted_frame = cv2.bitwise_not(pixelated_frame)

    # Create a binary mask where black pixels are foreground and white pixels are background
    _, mask = cv2.threshold(inverted_frame, 128, 255, cv2.THRESH_BINARY_INV)  # Inverted thresholding

    # Display the resulting frame
    cv2.imshow('Black Pixels on White Background', mask)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
