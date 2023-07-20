from googleapiclient.discovery import build
import json
from moviepy.editor import *
import os

class CreateClipVideo:
    def __init__(self, video_id):
        with open('./api.json', 'r') as f:
            config = json.load(f)
        api_key = config['api_key']
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.id = video_id
        self.i = 1
    
    def cut_video(self, start_time, end_time=None):
        if end_time is None:
            end_time = start_time + 60
        path = './output/'+self.id+'/'+self.id+'.mp4'
        clip = VideoFileClip(path).subclip(start_time, end_time)
        
        output_dir = './clip/'+self.id
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        clip_path = output_dir + '/' + self.id + '-' + str(self.i) +'.mp4'
        if os.path.exists(clip_path):
            self.i += 1
        
        clip.write_videofile(clip_path)
        clip.close()