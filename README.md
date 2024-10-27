
# FacePixel

**FacePixel** is a real-time pixelation and color inversion tool for video feeds. It captures live footage using a webcam, processes the frames to pixelate the image, and converts it into a black-on-white binary visual. The pixelated effect is achieved in real-time with adjustable pixel size for fine detail.

## Features

- Real-time video capture at 60 FPS.
- Black-on-white pixelation effect.
- Adjustable pixel size for better resolution.
- Color inversion (black pixels on a white background).
- Mirrored video for a more interactive experience.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:

```bash
git clone https://github.com/harsh11x/facepixel.git
```

2. Navigate to the directory:

```bash
cd facepixel
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the Python script:

```bash
python facepixel.py
```

Press 'q' to quit the live feed.

## How It Works

The video feed is captured in real-time from the webcam, mirrored horizontally, and then converted to grayscale. The pixelated effect is created by resizing the image to a smaller resolution and scaling it back up. A binary threshold is applied to achieve the black-on-white pixelation effect, and the result is displayed in a window.

## License

This project is licensed under the MIT License.
```

## Contributing

Feel free to open issues or submit pull requests to improve the project.

---

Created by Harsh Dev (@harsh11x).
