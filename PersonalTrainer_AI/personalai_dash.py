import streamlit as st
import pandas as pd 
from personal_ai import *

st.set_page_config(
  layout="wide"
)

personalAI = PersonalAI("IMG_2149.mov")
personalAI.run(True)

placeholder = st.empty()

status = "relaxed"
count = 0
while True:
  frame, landmarks, ts = personalAI.image_q.get()
  
  if len(landmarks.pose_landmarks) > 0:
    
    frame, elbow_angle = personalAI.find_angle(frame, landmarks, 12, 14, 16, True)
    frame, hip_angle = personalAI.find_angle(frame, landmarks, 11, 23, 25, True)
    
    # Pushup Logic
    if elbow_angle > 150 and hip_angle > 170:
      status = "ready"
      dir = "down"
    if status == "ready":
      if dir == "down" and elbow_angle < 60:
        dir = "up"
        count += 0.5
      if dir == "up" and elbow_angle > 100:
        dir == "down"
        count += 0.5
    
    with placeholder.container():
      col1, col2 = st.columns([0.4, 0.6])
      
      col1.image(frame)
      col2.markdown("### **status:** " + status)
      col2.markdown(f'### Count: {int(count)}')