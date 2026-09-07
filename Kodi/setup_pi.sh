#!/usr/bin/env bash
set -Eeuo pipefail

PROJECT_DIR="${HOME}/mediapipe_test"
VENV_DIR="${PROJECT_DIR}/venv"

echo "============================================================"
echo " Pi 5 + Bookworm + Picamera2 + MediaPipe setup"
echo "============================================================"

# ---------- Basic platform checks ----------
ARCH="$(uname -m)"
CODENAME="$(. /etc/os-release && echo "${VERSION_CODENAME:-unknown}")"
PYVER="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

if [[ "$ARCH" != "aarch64" ]]; then
    echo "ERROR: Expected 64-bit Raspberry Pi OS (aarch64), got: $ARCH"
    exit 1
fi

if [[ "$CODENAME" != "bookworm" ]]; then
    echo "ERROR: Expected Raspberry Pi OS Bookworm, got: $CODENAME"
    exit 1
fi

if [[ "$PYVER" != "3.11" ]]; then
    echo "ERROR: Expected Python 3.11 on Bookworm, got: $PYVER"
    exit 1
fi

echo "Platform OK: $ARCH / Bookworm / Python $PYVER"

# ---------- System packages ----------
echo
echo "[1/6] Installing Raspberry Pi / Python system packages..."

sudo apt update
sudo apt install -y \
    python3-full \
    python3-venv \
    python3-picamera2 \
    python3-opencv \
    python3-numpy \
    python3-simplejpeg

# Verify system camera Python stack before touching pip.
echo
echo "[2/6] Verifying system Picamera2 + NumPy..."

PYTHONNOUSERSITE=1 python3 - <<'PY'
import numpy
from picamera2 import Picamera2

print("System NumPy:", numpy.__version__, numpy.__file__)
print("System Picamera2: OK")
PY

# ---------- Fresh project / venv ----------
echo
echo "[3/6] Creating clean virtual environment..."

mkdir -p "$PROJECT_DIR"
rm -rf "$VENV_DIR"

python3 -m venv --system-site-packages "$VENV_DIR"

# Do not allow ~/.local Python packages to leak into this environment.
if ! grep -q '^export PYTHONNOUSERSITE=1$' "$VENV_DIR/bin/activate"; then
    echo 'export PYTHONNOUSERSITE=1' >> "$VENV_DIR/bin/activate"
fi

# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"
export PYTHONNOUSERSITE=1

python -m pip install --upgrade pip

# ---------- MediaPipe ----------
echo
echo "[4/6] Installing MediaPipe 0.10.14..."

# Install dependencies first in the normal way.
python -m pip install "mediapipe==0.10.14"

# We deliberately do NOT use pip's NumPy/OpenCV builds here.
# Picamera2/simplejpeg are compiled against Raspberry Pi OS's NumPy.
python -m pip uninstall -y numpy opencv-python opencv-contrib-python opencv-python-headless 2>/dev/null || true

# MediaPipe pulls Matplotlib. Newer Matplotlib releases require newer NumPy,
# so replace it with the version known to work with Bookworm's NumPy 1.24.2.
python -m pip uninstall -y matplotlib 2>/dev/null || true
python -m pip install --no-deps "matplotlib==3.7.5"

# ---------- Verification ----------
echo
echo "[5/6] Verifying final Python environment..."

python - <<'PY'
import sys
import numpy
import cv2
import matplotlib
import mediapipe as mp
from picamera2 import Picamera2

print("Python:       ", sys.version.split()[0])
print("NumPy:        ", numpy.__version__, numpy.__file__)
print("OpenCV:       ", cv2.__version__, cv2.__file__)
print("Matplotlib:   ", matplotlib.__version__, matplotlib.__file__)
print("MediaPipe:    ", mp.__version__, mp.__file__)
print("mp.solutions: ", hasattr(mp, "solutions"))

if not hasattr(mp, "solutions"):
    raise RuntimeError("MediaPipe mp.solutions API is unavailable")

print("Picamera2:     OK")
PY

# ---------- Test program ----------
echo
echo "[6/6] Writing hand-tracking test program..."

cat > "$PROJECT_DIR/test_mediapipe.py" <<'PY'
import cv2
import mediapipe as mp
from picamera2 import Picamera2

print("MediaPipe version:", mp.__version__)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

picam2 = Picamera2()
config = picam2.create_preview_configuration(
    main={"format": "RGB888", "size": (640, 480)}
)
picam2.configure(config)
picam2.start()

print("Camera started.")
print("Show your hand to the camera.")
print("Press Q to quit.")

try:
    while True:
        frame = picam2.capture_array()
        results = hands.process(frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                )

        display = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imshow("MediaPipe Hands - Raspberry Pi 5", display)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    hands.close()
    picam2.stop()
    cv2.destroyAllWindows()
PY

echo
echo "============================================================"
echo " Setup completed successfully."
echo "============================================================"
echo
echo "First test the camera:"
echo "  rpicam-hello"
echo
echo "Then run MediaPipe:"
echo "  cd \"$PROJECT_DIR\""
echo "  source venv/bin/activate"
echo "  python test_mediapipe.py"
echo
