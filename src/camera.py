import cv2

class Camera:
    """
    Camera class to capture frames from a USB camera or Raspberry Pi Camera.
    """
    def __init__(self, camera_index=0):
        """
        :param camera_index: If you use a USB camera, usually 0 or 1.
                             If you use Pi Camera Module, 
                             you might use the 'libcamera' approach or a different pipeline.
        """
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise RuntimeError("Cannot open camera. Check camera_index or hardware connection.")

    def get_frame(self):
        """
        Capture a single frame.
        """
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to read frame from camera.")
        return frame

    def release(self):
        """
        Release the camera resource.
        """
        if self.cap.isOpened():
            self.cap.release()
