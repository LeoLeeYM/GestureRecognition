# GestureControl - MediaPipe-Based Hand Gesture Recognition & Control

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-orange)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8.9%2B-green)

## Project Overview

This project implements real-time hand gesture recognition using MediaPipe's hand tracking technology. Through computer vision and gesture mapping, it enables various human-computer interaction scenarios including screen control, media operations, and text input.

## Key Features

### Supported Gestures
- ✋ Open Hand: Screenshot capture
- 👊 Fist: Trigger screen operations
- 👇 Downward Glide: Page scrolling
- 🤏 Pinching Gesture: Volume control
- 🤞 United Fingers: Mouse movement
- →← Lateral Spread: Media control

### System Operations
- Screen capture
- Volume adjustment
- Media control (next/previous)
- Mouse movement control
- Auto text input
- Page scrolling

## Quick Start

### Requirements
- Python 3.7+
- Webcam

### Install Dependencies
```bash
pip install opencv-python mediapipe pyautogui pywin32
```

### Run Application
```bash
python core.py
```

## Usage Guide
1. Ensure proper camera functionality
2. Keep hands within camera view
3. Use standard gesture patterns:
   - **Open Hand → Fist**: Take screenshot
   - **Backward Open → Open**: Page up
   - **Vertical Pinch Movement**: Volume control
   - **United Fingers Movement**: Mouse control
   - **Lateral Spread Switch**: Media control (left/right)

## Code Structure
```
GestureControl/
├── core.py            # Main entry
├── data.py            # Gesture data processing
├── gestureLib.py      # Gesture definitions
├── handle.py          # Gesture handlers
└── tool.py            # Utility functions
```

## Technical Approach
1. **Hand Detection**: MediaPipe Hands model for 21-landmark tracking
2. **Data Processing**: Calculate finger joint coordinates and geometric features
3. **Gesture Recognition**: Threshold-based pattern matching
4. **Action Mapping**: System operations via pyautogui

## Development Docs

### Key Parameters
- `distanceCoefficient`: Dynamic scaling factor
- `fingerOriginDiff`: Finger-to-palm offsets
- `fingerJointAverage`: Average joint positions

### Extending Gestures
1. Add new gesture conditions in `gestureLib.py`
2. Implement handlers in `handle.py`
3. Update state transition logic

## Contribution
We welcome contributions via Issues or PRs:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## Notes
- pyautogui FAILSAFE is disabled by default
- Recognition accuracy depends on lighting conditions
- Admin privileges required for some system operations

## License
[MIT License](LICENSE)

---

**Tip**: Recommended to run in Python virtual environment. MediaPipe pretrained models (~10MB) will be auto-downloaded on first run.
