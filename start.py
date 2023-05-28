import bh3
import os

video_folder = 'videos'
video_type = 'mp4'
video_paths = [os.path.join(video_folder, filename) for filename in os.listdir(
    video_folder) if filename.endswith(f'.{video_type}')]
for video in video_paths:
    bh3.extract(video)
