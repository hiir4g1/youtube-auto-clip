from googleapiclient.discovery import build
import json
from moviepy.editor import *
import os

class CreateClipVideo:
    def __init__(self, video_id: str, config_path: str = './api.json'):
        """Initializes CreateClipVideo with YouTube API access and video ID.

        Args:
            video_id: A string representing the YouTube video ID.
            config_path: Path to the json file containing API config. Defaults to './api.json'.
        """
        self.api_key = self._load_config(config_path)
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.id = video_id
        self.clip_counter = 1
    
    @staticmethod
    def _load_config(config_path: str) -> str:
        """Loads API key from configuration file.

        Args:
            config_path: Path to the configuration file.

        Returns:
            The API key as a string.

        Raises:
            FileNotFoundError: If the configuration file is not found.
            KeyError: If the 'api_key' is missing in the configuration file.
        """
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            return config['api_key']
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file {config_path} not found.")
        except KeyError:
            raise KeyError("'api_key' missing in configuration file.")
    
    def _prepare_output_dir(self, output_dir: str):
        """Creates an output directory if it does not exist.

        Args:
            output_dir: The directory to create.

        Raises:
            OSError: If the directory cannot be created.
        """
        if not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir)
            except OSError:
                raise OSError(f"Unable to create directory: {output_dir}")

    def cut_video(self, start_time: int, end_time: int = None):
        """Cuts a portion of the video and saves it in the output directory.

        Args:
            start_time: The start time of the clip in seconds.
            end_time: The end time of the clip in seconds. If not provided, it defaults to 60 seconds after the start_time.

        Raises:
            IOError: If the input video file is not found or the output file cannot be created.
        """
        if end_time is None:
            end_time = start_time + 60
        path = f'./output/{self.id}/{self.id}.mp4'
        
        try:
            clip = VideoFileClip(path).subclip(start_time, end_time)
        except IOError:
            raise IOError(f"Unable to load video file: {path}")
        
        output_dir = f'./clip/{self.id}'
        self._prepare_output_dir(output_dir)
        
        clip_path = f'{output_dir}/{self.id}-{self.clip_counter}.mp4'
        if os.path.exists(clip_path):
            self.clip_counter += 1
            clip_path = f'{output_dir}/{self.id}-{self.clip_counter}.mp4'
        
        try:
            clip.write_videofile(clip_path)
            clip.close()
        except IOError:
            raise IOError(f"Unable to create clip file: {clip_path}")
