from moviepy.editor import *

def create_upload_video(img_path,video_path,output_path):
    clip1 = ImageClip(img_path).set_duration('00:00:58.00')
    clip2 = VideoFileClip(video_path)
    clip = CompositeVideoClip([clip1,clip2.set_position(("center", "center"))])
    
    clip.write_videofile(output_path)
    clip.close()