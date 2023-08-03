import cv2
import mediapipe as mp
from mediapipe.tasks import python
import numpy as np

from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

file_name = 'IMG_2149.mov'
model_path = 'pose_landmarker_full.task'


def draw_landmarks_on_image(rgb_image, detection_result):
  pose_landmarks_list = detection_result.pose_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected poses to visualize.
  for idx in range(len(pose_landmarks_list)):
    pose_landmarks = pose_landmarks_list[idx]

    # Draw the pose landmarks.
    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      pose_landmarks_proto,
      solutions.pose.POSE_CONNECTIONS,
      solutions.drawing_styles.get_default_pose_landmarks_style())
  return annotated_image

# https://developers.google.com/mediapipe/solutions/vision/pose_landmarker/python#video
options = python.vision.PoseLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=model_path),
    running_mode=python.vision.RunningMode.VIDEO
)

with python.vision.PoseLandmarker.create_from_options(options) as landmarker:
    cap = cv2.VideoCapture(file_name)
    calc_timestamps = [0.0]
    
    while (cap.isOpened()):
        ret, frame = cap.read()
        fps = cap.get(cv2.CAP_PROP_FPS)

        if ret == True:
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            calc_timestamps.append(int(calc_timestamps[-1] + 1000/fps))
            detection_result = landmarker.detect_for_video(mp_image, calc_timestamps[-1])
            
            frame= draw_landmarks_on_image(frame, detection_result)
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()